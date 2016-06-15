from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^articles/$', views.article_list, name='article_list'),
	url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
	url(r'^lessons/$', views.lesson_list, name='lesson_list'),
	url(r'^lesson/(?P<pk>[0-9]+)/$', views.lesson_detail, name='lesson_detail'),
	url(r'^categories/$', views.category_list, name='category_list'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.category_detail, name='category_detail'),

]