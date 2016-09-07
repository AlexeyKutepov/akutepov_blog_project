__author__ = 'Alexey Kutepov'

from django.conf.urls import patterns, url
from feedback import views

urlpatterns = patterns('',
        url(r'^feedback/$', views.feedback, name='feedback'),
)