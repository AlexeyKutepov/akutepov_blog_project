__author__ = 'Alexey Kutepov'

from django.conf.urls import patterns, url
from subscribe import views

urlpatterns = patterns('',
        url(r'^add/$', views.subscribe_add, name='subscribe_add'),
)
