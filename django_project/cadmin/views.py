from django.shortcuts import render, redirect
from blog.forms import PostForm
from blog.models import Post, Author, Category, Tag
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django_project import helpers
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings


# Create your views here.


def post_add(request):
    
    # if request is POST, create a bound form (form with data)
    
    if request.method == "POST":
        f = PostForm(request.POST)
        
        # check whether form is valid
        # if valid, save data to database
        # redirect user back to add post form
        
        # if form is invalid show form with errors
        if f.is_valid():
            # save data
            f.save()
            return redirect('post_add')
        
    # if request is GET then show unbound form to user
    else:
        f = PostForm()
    return render(request, 'cadmin/post_add.html', {'form': f})

@login_required
def home(request):
#    if not request.user.is_authenticated:
#        return redirect('login')
    
    return render(request, 'cadmin/admin_page.html')

def login(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('/cadmin/')
    else:
        return auth_views.login(request, **kwargs)
    
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            # send email verification
            activation_key = helpers.generation_activation_key(username=request.POST['username'])
            
            subject = "App Verification"
            
            message = '''\n
            Please click to verify your account \n\n{0}://{1}/cadmin/activate/account/?key={2}'''.format(request.scheme, request.get_host(), activation_key)
            
            error = False
            
            try:
                send_mail(subject, message, settings.SERVER_EMAIL, [request.POST['email']])
                messages.add_message(request, messages.INFO, 'Account created! Click on the link sent to your email to activate your account.')
                
            except: 
                error = True
                messages.add_message(request, messages.INFO, 'Unable to send email verification. Please try again later.')
                
            if not error:
                u = User.objects.create_user(
                    request.POST['username'],
                    request.POST['email'],
                    request.POST['password1'],
                    is_active = 0
                )
                
                author = Author()
                author.activation_key = activation_key
                author.user = u
                author.save()
            
            return redirect('register')
            
            # f.save()
            # messages.success(request, 'Account created suvvessfully')
            # return redirect('register')
        
    else:
        f = CustomUserCreationForm()
        
    return render(request, 'cadmin/register.html', {'form': f})

def activate_account(request):
    key = request.GET['key']
    if not key:
        raise Http404()
        
    r = get_object_or_404(Author, activation_key=key, email_validated=False)
    r.user.is_active = True
    r.user.save()
    r.email_validated = True
    r.save()
    
    return render(request, 'cadmin/activated.html')