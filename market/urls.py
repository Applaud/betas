from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
                       (r'^$', views.survey),
                       (r'^results/$', views.results),
                       )
