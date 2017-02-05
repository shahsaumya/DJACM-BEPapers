

from django.contrib import admin
#from mysite.travel.models import Place
# Register your models here.


from login.models import Project, UserProfile,Teacher


admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Teacher)



