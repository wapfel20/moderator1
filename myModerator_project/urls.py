from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^google/', include('google_login.urls')),
    url(r'^moderator/', include('moderatorapp.urls')),
    #url(r'^someApp/', include(some_app.urls')),    
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#local views file
urlpatterns += patterns('myModerator_project.views',
    (r'^$', "index"),  # this catches the blank index
    (r'^dashboard/$', "dashboard"),
    (r'^splash/$', "splash"),
    (r'^forumView/(?P<forumID>\d+)/$', 'forumView'), # this captures a variable    
)