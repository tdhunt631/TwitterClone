from django.conf.urls import patterns, include, url
from microblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)