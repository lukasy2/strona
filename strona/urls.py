from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from newsy import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', views.register_user),
    url(r'^accounts/register_success/$', views.register_success),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'', include('newsy.urls')),
    url(r'^q/', include('quiz.urls')),
]


