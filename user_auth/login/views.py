from django.shortcuts import render
from user_auth.forms import ProjectForm
from django.http import HttpResponse
from login.models import Project, UserProfile
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from login.forms import UserForm, UserProfileForm, ProjectForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


@login_required
def index(request):
    return render(request,'index.html', {'view_is_index': True})

def works(request):
    return render(request,'works.html')
    


def about(request):
    return render(request,'about.html')    


def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    return render(request,'home.html')


def register(request):
    registered = False
    
    user_form = UserForm()
    profile_form = UserProfileForm()

    # Prevent logged in users from registering again
    if request.user.is_authenticated():
       return redirect(reverse('index'))

    else:
        return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    elif request.method == 'GET':
        print(request.user)
        if request.user.is_authenticated:
             return redirect(reverse('index'))
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
                return redirect(reverse('sign-in'))

            except:
                return redirect(reverse('sign-in'))

        else:
            print (user_form.errors, profile_form.errors)
            return redirect(reverse('register'))
    else: 
        return redirect(reverse('sign-in'))


@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        data = request.POST
        project = Project(title=data['title'], description=data['description'],
                          video_url=data['video'], pdf_url=data['pdf_url'], 
                          creator=UserProfile.objects.get(user=request.user))
        project.save()
        return redirect(reverse('index'))


@csrf_exempt
@login_required
def project_form(request):
    return render(request, 'services.html', 
            {'project_form': ProjectForm(),
             'username' : request.user.username,
             'view_is_upload': True})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('home'))


# View individual projects, searching by id
@login_required
def view_project(request, project_id, project_slug):
    try:
        project = Project.objects.get(id=project_id)
        context = project.to_dict()
        context['view_is_view'] = True
        context['creator_name'] = project.creator.user.first_name + ' ' + project.creator.user.last_name

        print (project.creator.user.__dict__)
        if project.active:
            return render(request, 'view-project.html', context)
        else:
            return redirect('/404/')

    except ObjectDoesNotExist:
        return redirect('/404/')
	return HttpResponse(project_id + project_slug)


# !!! This is a view only for testing, remove this in production
def all_projects(request):
    projects  = Project.objects.all()
    response = ''
    for project in projects:
        response+='<p><h1>' + project.title +\
                        '<span style="font-size: 18px; margin-left: 15px;">'\
                        '<a href="' + project.get_url() + '">Link</a></span>'\
                        '</h1></p>'
        print (project.get_url())
    return HttpResponse(response)