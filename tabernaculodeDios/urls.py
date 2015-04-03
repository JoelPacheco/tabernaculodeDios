from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'iglesia.views.login', name='login'),
    url(r'^login', 'iglesia.views.login', name='login'),
    url(r'^home', 'iglesia.views.home', name='home'),
    url(r'^usuario/registrousuario', 'iglesia.views.registrousuario', name='registrousuario'),
    url(r'^buscarubigeopornombre', 'iglesia.views.buscarubigeopornombre', name='buscarUbigeoPorNombre'),
    url(r'^usuario/detalleusuario', 'iglesia.views.detalleusuario', name='detalleusuario'),
    url(r'^usuario/detalleusuario(?P<id>\d+)/$', 'iglesia.views.detalleusuario', name='detalleusuario'),
    url(r'^usuario/detalleusuario(?P<id>\d+)(&P<mensaje>[1-4]+)/$', 'iglesia.views.detalleusuario',
        name='detalleusuario'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
