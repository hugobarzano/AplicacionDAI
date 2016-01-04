from django.conf.urls import patterns, url
from bares_y_tapas import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),#creo url para index y la aniado al nuevo fichero de urls de la aplicacion, asilandolas de
	url(r'^about/', views.about, name='about'),
	url(r'^todos/', views.todos, name='todos'),
    url(r'^details/(?P<nombre_bar>[\w\-]+)/$', views.details, name='details'),
	url(r'^bar/(?P<bar_nombre_slug>[\w\-]+)/$', views.bar, name='bar'),)
