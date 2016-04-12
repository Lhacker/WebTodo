from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

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

def index(request):
    return HttpResponse("index")
