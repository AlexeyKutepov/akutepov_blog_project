from cms.models.pluginmodel import CMSPlugin

from django.db import models

from filer.fields.image import FilerImageField


class Item(CMSPlugin):
    image = FilerImageField()
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.header
