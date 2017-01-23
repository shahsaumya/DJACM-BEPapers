

from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	#profile_pic = models.ImageField(uploadTo='profile_pic', blank=True)
	branch = models.TextField(max_length=30)
	domain = models.TextField(max_length=30)

	def __str__(self):
		return self.user.username



class Project(models.Model):
    project_name = models.TextField(max_length=100)
    project_document = models.FileField(null = True)

    def __str__(self):
        return self.project_name










