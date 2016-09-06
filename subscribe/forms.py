__author__ = 'Alexey Kutepov'

from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField()