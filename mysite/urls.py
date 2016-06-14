"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from mysite.views import hello,root,current_datetime,hours_ahead, share_chart_view, BarView, LineView
from django.contrib import admin
from django.contrib.auth import views as auth_views





admin.autodiscover()



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^share/([A - Z]{4,5})/$]', share_chart_view),
    url(r'^hello/$', hello),
    url(r'^$', root),
    url(r'^time/$', current_datetime),
    url(r'^share/$', share_chart_view),
    url(r'^bar/$', LineView.as_view(), name='bar'),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/', include('schedule.urls')),
    url(r'^time/plus/(\d{1,2})/(\d{1,2})/$', hours_ahead),
]


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()