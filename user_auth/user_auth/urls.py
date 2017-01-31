"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from login import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
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
    url(r'^login_form/$', views.login_form, name='login_form'),
    url(r'^new-project/$', views.project_form, name='new_project'),
    url(r'^add-project/$', views.add_project, name='add_project'),

 
#    url(r'^login/$', views.login, name='login'),
    url(r'^upload/$', views.project_form, name = 'upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

