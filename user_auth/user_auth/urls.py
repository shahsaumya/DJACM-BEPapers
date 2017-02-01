from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from login import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
=======

>>>>>>> ff56e7b3f6a1bea5db5a4ce6db32132a5546df8d
    url(r'^home/$', views.home),
    url(r'^index/$', views.index),
    url(r'^about/$', views.about),
    url(r'^works/$', views.works),
    
#    url(r'^search/$', views.search),
#    url(r'^contact/$',views.contact),
    url(r'^register/$',views.register, name='register'),
    url(r'^sign-in/$',views.user_login, name='sign-in'),
    url(r'^logout/$', views.user_logout, name='logout'),             
    url(r'^add-user/$', views.add_user, name='add_user'),
   # url(r'^login_form/$', views.login_form, name='login_form'),
    url(r'^new-project/$', views.project_form, name='new_project'),
    url(r'^add-project/$', views.add_project, name='add_project'),
<<<<<<< HEAD
=======

 

>>>>>>> ff56e7b3f6a1bea5db5a4ce6db32132a5546df8d
    url(r'^home/$', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
#    url(r'^search/$', views.search, name='search'),
#    url(r'^contact/$',views.contact, name='contact'),
    url(r'^register/$',views.register, name='register'),
    url(r'^sign-in/$',views.user_login, name='sign-in'),
    url(r'^logout/$', views.user_logout, name='logout'),             
    url(r'^add-user/$', views.add_user, name='add-user'),
    url(r'^new-project/$', views.project_form, name='new-project'),
    url(r'^add-project/$', views.add_project, name='add-project'),
<<<<<<< HEAD
=======

>>>>>>> ff56e7b3f6a1bea5db5a4ce6db32132a5546df8d
#    url(r'^login/$', views.login, name='login'),
    url(r'^upload/$', views.project_form, name = 'upload'),
    url(r'^view/(?P<project_id>\d+)/(?P<project_slug>[\w-]+)/$', views.view_project, name='view-project'),
    url(r'^all-projects/$', views.all_projects, name='all-projects'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)