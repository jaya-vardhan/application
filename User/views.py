from django.shortcuts import render
from .models import Post
from .forms import UserRegistrationForm,PostForm
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerView(request):   
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)    
        if form.is_valid():
            form.save()
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        uname=request.POST['username']
        pass1=request.POST['password']
        email=request.POST['email']       
        user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=pass1,email=email)
        user.save()
    context={
        'form':UserRegistrationForm
    }
    return render(request,'User/home.html',context)


@login_required
def homeView(request):
    post=Post.objects.using('user_db').all()
    if request.method == 'POST':
        form=PostForm(request.POST)    
        if form.is_valid():
            form.save()
    context={
        'form':PostForm,
        'posts':post
    }
    return render(request,'User/post.html',context)


 
