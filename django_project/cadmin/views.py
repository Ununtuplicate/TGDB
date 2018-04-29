from django.shortcuts import render, redirect
from blog.forms import PostForm
from blog.models import Post, Author, Category, Tag
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


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
            f.save()
            messages.success(request, 'Account created suvvessfully')
            return redirect('register')
        
    else:
        f = CustomUserCreationForm()
        
    return render(request, 'cadmin/register.html', {'form': f})