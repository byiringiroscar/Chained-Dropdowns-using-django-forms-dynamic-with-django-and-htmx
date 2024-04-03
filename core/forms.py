from django import forms
from .models import Course, Module



class UniverstiyForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        initial=Course.objects.first(),
        )