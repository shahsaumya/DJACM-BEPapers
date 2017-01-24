from login.models import UserProfile, Project
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('first_name','last_name','username','email','password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('branch','domain')

class ProjectForm(forms.ModelForm):
    class Meta: 
        model = Project
        fields = ('title', 'description', 'video_url')
        labels = {
                'title': ('Project Name'),
                'description':('Add a description'),
                'video_url': ('Add a video'),
                }
