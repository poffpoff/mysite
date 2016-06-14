# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout



urlpatterns = [
    url(r'schedule/$', TemplateView.as_view(template_name="schedule/base.html"), name='schedule'),
    url(r'profile/$', TemplateView.as_view(template_name="schedule/dashboard1.html"), name='dashboard'),
    url(r'dashboard1/$', TemplateView.as_view(template_name="schedule/dashboard4.html"), name='dashboard1'),
    url(r'dashboard2/$', 'schedule.views.get_special_user', name='dashboard2'),
    url(r'getEvent/$', 'schedule.views.get_event', name='getEvent'),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
    url(r'^events.json$', 'schedule.views.events_json', name='events.json'),
    url(r'^events.map.json(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})$', 'schedule.views.events_map_json', name='events.map.json'),
    url(r'^events.map.update.json(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})$', 'schedule.views.events_map_update_json', name='events.map.update.json'),
    url(r'^globe/', TemplateView.as_view(template_name="schedule/globe.html"), name='globe'),
    url(r'^event/', TemplateView.as_view(template_name="schedule/event.html"), name='event'),

]