from django.shortcuts import render, redirect
from blog.forms import PostForm


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