from django.conf.urls import patterns, include, url
from survey.views import thanks, survey, results, login
from testapp.views import send_surveys, receive_response, all_surveys, form_create, all_responses
from django.contrib import admin
import settings
import buds
import buds.urls
import coffeand
import coffeand.urls
import tahoekayak
import tahoekayak.urls
import market
import market.urls
admin.autodiscover()

urlpatterns = patterns('',
                       #(r'^$', survey),
                       (r'^buds/', include(buds.urls)),
                       (r'^coffee&/', include(coffeand.urls)),
                       (r'^kayak/', include(tahoekayak.urls)),
                       (r'obexersmarket/', include(market.urls)),
                       # (r'^results/$', results),
                       (r'^login/$', login),
                       (r'^thanks/', thanks),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT}),
                       # (r'^testapp/survey-data$', send_surveys),
                       # (r'^testapp/response$', receive_response),
                       # (r'^testapp/surveys$', all_surveys),
                       # (r'^testapp/create$', form_create),
                       # (r'^testapp/results$', all_responses),
                       )
