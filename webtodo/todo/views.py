from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

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
    todo_list = Todo.objects.filter(user = request.user).order_by('order')
    return render(request, 'todo/index.html', {
        'todo_list': todo_list
    })

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'

class EditView(generic.UpdateView):
    model = Todo
    fields = ['todo_text']
    template_name = 'todo/edit.html'
    success_url = reverse_lazy('todo:index')
