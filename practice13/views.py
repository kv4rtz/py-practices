from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from .models import Profile

@login_required(login_url='login')
def profile_view(req: HttpRequest):
    user = Profile.objects.select_related('user').get(user=req.user)

    if req.method == 'POST':
        user.gender = req.POST['gender']
        user.country = req.POST['country']
        user.city = req.POST['city']
        user.street = req.POST['street']
        user.house = req.POST['house']
        user.apartment_number = req.POST['apartment_number']

        user.save()

        
    return render(req, 'p13_profile.html', {
        'user': user
    })

