from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'iglesia.views.login', name='login'),
    url(r'^login', 'iglesia.views.login', name='login'),
    url(r'^home', 'iglesia.views.home', name='home'),
    url(r'^registrousuario', 'iglesia.views.registrousuario', name='registrousuario'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
)
