from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.quiz_list, name='quiz_list'),
	url(r'^(?P<pk>[0-9]+)/$', views.quiz_detail, name='quiz_detail'),

]