from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import RegisterForm
from django.contrib.auth.models import User

def register(req: HttpRequest):
    if (req.method == 'POST'):
        form = RegisterForm(req.POST)
        print(form.errors.as_text())
        # Qfkdjsfs89453GFDJMl;fdsfsd54
        if form.is_valid():
            User.objects.create_user(
                username=form.data.get('username'),
                email=form.data.get('email'),
                password=form.data.get('password1')
            )

            return redirect('home')
        
        return redirect('register')
    else:
        form = RegisterForm()
        return render(req, 'p11_register.html', {
            'form': form
        })