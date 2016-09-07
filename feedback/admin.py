from django.contrib import admin

# Register your models here.
from feedback.models import Feedback


@admin.register(Feedback)
class Feedback(admin.ModelAdmin):
    list_display = ('email', 'message', 'datetime', )
    list_filter = ('email', 'datetime', )