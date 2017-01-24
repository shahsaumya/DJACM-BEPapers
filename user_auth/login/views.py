from django.shortcuts import render
from user_auth.forms import ProjectForm
from django.http import HttpResponse
from login.models import Project, UserProfile
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from login.forms import UserForm, UserProfileForm, ProjectForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import Project

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')


def register(request):
    #context = RequestContext(request)
    registered = False
    
    user_form = UserForm()
    profile_form = UserProfileForm()

    if request.user.is_authenticated():
        return redirect('/index/')

    else:
        return render(
                      request,
                      'register.html',
                      {'user_form': user_form, 
                       'profile_form': profile_form, 
                       'registered': registered
                      })


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('/index/')
            else:
                return redirect("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    #else:
    #    return render(request, 'sign-in.html', {})


@csrf_protect
def login_form(request):
    if request.user.is_authenticated():
        return redirect('/index/')
    else:
        return render(request, 'sign-in.html', {})


def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            try:
                user.set_password(user.password)
                user.save()
                
                profile = profile_form.save(commit=False)
                profile.user = user
                 
                profile.save()
                registered = True
                return redirect('/sign-in/')

            except:
                return redirect('/sign-in/')

        else:
            print (user_form.errors, profile_form.errors)
            return redirect('/register')
    else: 
        return redirect('/sign-in/')

@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        data = request.POST
        project = Project(title=data['title'], description=data['description'],
                          video_url=data['video'], pdf_url=data['pdf_url'], 
                          creator=UserProfile.objects.get(user=request.user))
        project.save()
        return redirect('/index/')


@csrf_exempt
@login_required
def project_form(request):
    return render(request, 'project-form.html', 
            {'project_form': ProjectForm(),
             'username' : request.user.username})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/home/')
