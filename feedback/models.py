from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


