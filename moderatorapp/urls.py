from django.conf.urls import patterns, include, url

#local views file
urlpatterns = patterns('moderatorapp.views',
    (r'^createForum/$', "createForum"),
    (r'^createPost/$', "createPost"),
    (r'^createComment/$', "createComment"),
    (r'^adjustRating/$', "adjustRating"),
)