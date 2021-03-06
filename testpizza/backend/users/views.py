from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    print(request.user)
    if not request.user.is_authenticated:
        return render(request, 'users/login.html', {'message': None})
    context = {
        'user': request.user
    }
    return render(request, 'users/user.html', context)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('users:index'))
    else:
        return render(request, 'users/login.html', {'message': 'Invalid credentials.'})


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {'message': 'Logged out.'})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('pizza:home')
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})