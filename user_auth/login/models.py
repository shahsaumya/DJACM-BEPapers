from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    DEPARTMENTS = (
            ('CO', 'COMPUTERS'),
            ('IT', 'INFORMATION TECHNOLOGY'),
            ('EC', 'ELECTRICAL'),
            ('EX', 'ELECTRONICS AND TELECOMMUNICATION'),
            ('BI', 'BIOMEDICAL'),
            ('PR', 'PRODUCTION'),
            ('ME', 'MECHANICAL'),
            ('CH', 'CHEMICAL'),
            )

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    #profile_pic = models.ImageField(uploadTo='profile_pic', blank=True)
    branch = models.CharField(max_length=2, choices=DEPARTMENTS, default='CO')
    domain = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=300, default='Untitled Project')
    pdf_url = models.URLField(max_length=600, editable=False, default=None)
    video_url = models.URLField(max_length=600, default=None)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    description = models.TextField(default='')
    slug = models.SlugField(max_length=75, editable=False, default='untitled-project')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:75] 
                            if len(self.title) > 
                            75 else self.title)

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
