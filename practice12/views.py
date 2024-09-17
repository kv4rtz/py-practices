from django.shortcuts import redirect, render
from django.http import HttpRequest
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def login_user(req: HttpRequest):
    if req.method == 'POST':
        form = LoginForm(req, data=req.POST)

        user = User.objects.get(username=req.POST['username'])
        print(user.check_password(req.POST['password']))
        if user is not None:
            if user.check_password(req.POST['password']):
                login(req, user)

                return redirect('home')

        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(req, user)

                return redirect('home')
        return redirect('login')    
    else:
        form = LoginForm(req)
        return render(req, 'p12_login.html', {
            "form": form
        })

def logout_user(req: HttpRequest):
    if req.method == 'POST':
        logout(req)
    
    return redirect('home')