# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView




# -*- coding: utf-8 -*-
from django import http
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
import simplejson as json
from django.utils import timezone
from django.contrib.auth.models import User
from schedule.models import Event, MySpecialUser


from django.contrib import auth



def login_view(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(email=email, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")

def events_json(request):
    # Get all events - Pas encore terminé
    users = MySpecialUser.objects.all()

    # Get all events - Pas encore terminé
    events = Event.objects.all()

    # Create the fullcalendar json events list
    event_list = []

    for user in users:
        for event in events:
            # On récupère les dates dans le bon fuseau horaire
            event_start = event.start.astimezone(timezone.get_default_timezone())
            event_end = event.end.astimezone(timezone.get_default_timezone())

            # On décide que si l'événement commence à minuit c'est un
            # événement sur la journée
            if event_start.hour == 0 and event_start.minute == 0:
                allDay = True
            else:
                allDay = False

            if not event.is_cancelled:
                event_list.append({
                        'id': event.id,
                        'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                        'end': event_end.strftime('%Y-%m-%d %H:%M:%S'),
                        'title': event.title,
                        'allDay': allDay
                        })

    if len(event_list) == 0:
        raise http.Http404
    else:
        return http.HttpResponse(json.dumps(event_list),
                                 content_type='application/json')

from datetime import datetime

def events_map_json(request, date):
    date_to_display = date + ' 00:00'
    # Get all events - Pas encore terminé
    users = MySpecialUser.objects.all()
    events = Event.objects.get(start=date_to_display)
    # Create the fullcalendar json events list
    location_list = []

    for user in users:
        location_list.append({
            'lat': user.city.latitude,
            'long': user.city.longitude,
            'text1': user.user.username,
            'text2': "What I am doing in " + user.city.name + " : Living",
            'text3': "How to contact me :" + user.user.email
            })

    if len(location_list) == 0:
        raise http.Http404
    else:
        return http.HttpResponse(json.dumps(location_list),
                                 content_type='application/json')


def events_map_update_json(request, date):
    # Get all events - Pas encore terminé
    users = MySpecialUser.objects.all()

    # Create the fullcalendar json events list
    location_list = []

    for user in users:
        location_list.append({
            'lat': user.city.latitude,
            'long': user.city.longitude,
            'text1': user.user.username,
            'text2': "TEST What I am doing in " + user.city.name + " : Living",
            'text3': "TEST How to contact me :" + user.user.email
            })

    if len(location_list) == 0:
        raise http.Http404
    else:
        return http.HttpResponse(json.dumps(location_list),
                                 content_type='application/json')



from django.shortcuts import render
from django.http import HttpResponseRedirect

from schedule.form import MySpecialUserForm, EventForm

def get_special_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MySpecialUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MySpecialUserForm()

    return render(request, 'schedule/dashboard2.html', {'form': form})

def get_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()

    return render(request, 'schedule/event.html', {'form': form})

