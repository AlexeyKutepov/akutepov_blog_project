from cms.models.pluginmodel import CMSPlugin

from django.db import models


class ServiceItem(CMSPlugin):
    title = models.CharField(max_length=100)
    details = models.TextField()
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.title
