from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

# login_required permite ocultar la vista hasta que se este logueado


@login_required
def index(request):
    return render(request, 'home.html')


def exit(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html', {
            'form': UserCreationForm
            })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                return HttpResponse(' usuario creado')

            except:
                return HttpResponse('existe')
        return HttpResponse('Problema Arrecho, escriba bien')
