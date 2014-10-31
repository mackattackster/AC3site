from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ac3app.models import Event, UserProfile, UserSession
from django.contrib.auth import logout, authenticate, login
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import emails


def index(request):
    try:
        if request.COOKIES['logged'] == 'temp':
            return HttpResponseRedirect('/ac3app/mainview/')
    except KeyError:
        pass
    return render(request, 'ac3app/login.html')


@login_required(login_url='/ac3app/')
def main_view(request):
    latest_events = Event.objects.order_by('-date_created')[:5]
    latest_events_json = serializers.serialize('json', Event.objects.all(), use_natural_foreign_keys=True,
                                               use_natural_primary_keys=True)
    context = {'latest_events': latest_events, 'latest_events_json': latest_events_json}
    return render(request, 'ac3app/MainView.html', context)

@login_required(login_url='/ac3app/')
def profile_view(request):
    requesting_user = User.objects.get_by_natural_key(request.user)
    context = {'user': requesting_user}
    return render(request, 'ac3app/profile.html', context)


def login_view(request):
    if request.method == 'POST':
        if 'login_sub' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    request.session.set_expiry(300)
                    h = HttpResponseRedirect('/ac3app/mainview')
                    #TODO: Figure out a better way to save secure user cookies
                    h.set_cookie('logged', 'temp', max_age=120)
                    return h
                else:
                    return HttpResponse('Account disabled.')
            else:
                messages.add_message(request, messages.ERROR, 'Incorrect username or password!')
                return HttpResponseRedirect('/ac3app/')
                #return render(request, 'ac3app/login.html')
        elif 'forgot_password_sub' in request.POST:
            return emails.forgot_password_email(request)
        else:
            return render(request, 'ac3app/login.html')


@login_required(login_url='/ac3app/login/')
def user_logout(request):
    logout(request)
    request.session.flush()
    messages.add_message(request, messages.SUCCESS, 'You have now successfully logged out.')
    h = HttpResponseRedirect('/ac3app/')
    #TODO: Need to find a way to remove secure logged in user cookie
    h.delete_cookie('logged')
    return h
