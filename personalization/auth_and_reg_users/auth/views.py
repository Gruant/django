from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm


def home(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.get_username()
    return render(
        request,
        'home.html',
        context
    )


def view_signup(request):
    if request.method == 'POST':
        register_form = SignupForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = SignupForm()

    context = {
        'form': register_form
    }

    return render(
        request,
        'signup.html',
        context
    )


def view_login(request):
    if request.method == 'POST':
        register_form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        register_form = LoginForm()
    context = {
        'form': register_form
    }

    return render(
        request,
        'login.html',
        context
    )


def view_logout(request):
    logout(request)
    return render(
        request,
        'logout.html'
    )

