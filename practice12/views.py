from django.shortcuts import redirect, render
from django.http import HttpRequest
from .forms import LoginForm
from django.contrib.auth import login

def login_user(req: HttpRequest):
    if req.method == 'POST':
        form = LoginForm(req, data=req.POST)
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
