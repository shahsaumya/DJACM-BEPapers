

from django import forms
from django.contrib.auth.models import User
 
class ProjectForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField()
    notes = forms.CharField()
    image = forms.FileField()



