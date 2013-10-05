from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^users', RedirectView.as_view(url='/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^', include('microblog.urls', namespace='microblog')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

