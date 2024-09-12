from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import RegisterForm

def register(req: HttpRequest):
    if (req.method == 'POST'):
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            user.save()

            return redirect('home')
        
        return redirect('register')
    else:
        form = RegisterForm()
        return render(req, 'p11_register.html', {
            'form': form
        })