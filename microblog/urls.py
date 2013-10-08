from django.conf.urls import patterns, include, url
from microblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^detail/(?P<user>\d+)/$', views.detail, name='detail'),
	url(r'^addPost/(?P<profile_id>\d+)/$', views.addPost, name='addPost'),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^createProfile/$', views.createProfile, name="createProfile"),
    url(r'^updateProfile/$', views.updateProfile, name="updateProfile"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
