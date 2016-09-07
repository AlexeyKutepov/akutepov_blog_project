__author__ = 'Alexey Kutepov'

from django import forms


class FeedbackForm(forms.Form):
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)