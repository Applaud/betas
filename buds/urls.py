from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
                       (r'^results/$', views.results),
                       (r'^$', views.survey),
                       )
