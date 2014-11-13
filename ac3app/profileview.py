from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from ac3app.models import UserProfile


@login_required(login_url='/ac3app/')
def profile_view(request):
    user = User.objects.get_by_natural_key(request.user)
    userProfile = UserProfile.objects.get(user = user)
    if(user.is_staff):
        userslist = User.objects.all()
        userslist = list(userslist)
    else:
        userslist = None

    if request.method == 'POST':
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        userProfile.user_pin = request.POST['userpin']
        userProfile.phone_number = request.POST['phonenumber']
        userProfile.save()
        user.save()
    context = {'user': user,
               'userProfile': userProfile,
               'userslist': userslist
               }
    return render(request, 'ac3app/profile.html', context)
