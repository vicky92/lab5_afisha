from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'l4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Films.views.GetMain'),
    url(r'^select/film/$', 'Films.views.GetAllFilm'),
    url(r'^select/cinema/$', 'Films.views.GetAllCinema'),
    url(r'^select/session/$', 'Films.views.GetAllSession'),
    url(r'^update/film/(\w*)/$',    'Films.views.UpdateFilm'),
    url(r'^update/cinema/(\w*)/$',    'Films.views.UpdateCinema'),
    url(r'^update/session/(\w*)/$',    'Films.views.UpdateSession'),
    url(r'^delete/film/(\w*)/$', 'Films.views.DeleteFilm'),
    url(r'^delete/cinema/(\w*)/$', 'Films.views.DeleteCinema'),
    url(r'^delete/session/(\w*)/$', 'Films.views.DeleteSession'),
    url(r'^add/film/$', 'Films.views.CreateFilm'),    
    url(r'^add/cinema/$', 'Films.views.CreateCinema'),    
    url(r'^add/session/$', 'Films.views.CreateSession'),   
    url(r'^film/(\w*)/$', 'Films.views.GetFilmInfo'),    
    url(r'^cinema/(\w*)/$', 'Films.views.GetCinemaInfo'),    
    url(r'^session/(\w*)/$', 'Films.views.GetSessionInfo'),     
)
