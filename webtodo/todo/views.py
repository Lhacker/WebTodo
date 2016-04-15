from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Todo

# Create your views here.
def login(request):
    from django.contrib.auth import login

    user = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('todo:index'))

    return render(request, 'todo/login.html', {
        'user': user
    })

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('todo:login'))

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseBadRequest('Please login from ' + reverse('todo:login'))

    todo_list = Todo.objects.filter(user = request.user).order_by('order')
    return render(request, 'todo/index.html', {
        'todo_list': todo_list
    })

@csrf_exempt
@transaction.atomic
def save(request):
    if not request.user.is_authenticated():
        return HttpResponseBadRequest('Please login from ' + reverse('todo:login'))

    received_json_data = json.loads(request.body.decode('utf8'))

    # register new todo
    for new_todo in received_json_data['newTodos']:
        t = Todo(
            user = request.user,
            todo_text = new_todo['todoText'],
            order = new_todo['order'],
        )
        t.save()

    # update todo order
    for todo in received_json_data['updateTodos']:
        t = Todo.objects.get(pk = todo['todoId'])
        t.order = todo['order']
        t.save()

    # delete todo
    for todo_id in received_json_data['deleteTodoIds']:
        Todo.objects.get(pk = todo_id).delete()

    return HttpResponse("ok")

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'

class EditView(generic.UpdateView):
    model = Todo
    fields = ['todo_text']
    template_name = 'todo/edit.html'
    success_url = reverse_lazy('todo:index')
