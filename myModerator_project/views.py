from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from google_login.models import GoogleUserInfo
from moderatorapp.models import Forum, ModUser, Post, Comment

def index(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        if User.objects.filter(id=user_id):
            user = User.objects.get(id=user_id)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect("/dashboard/")
        
        else:
            user_id = False
    else:
        user_id = False
    
    if not user_id:
        return redirect('/splash/')

@login_required
def dashboard(request):
    if GoogleUserInfo.objects.filter(user=request.user):
        userInfo = GoogleUserInfo.objects.get(user=request.user)
    else:
        userInfo = False
        
        
    if ModUser.objects.filter(user=request.user):
        modUser = ModUser.objects.get(user=request.user)
    else:
        modUser = False
        
    if Forum.objects.filter(ownerID=modUser.id):
        myForums = Forum.objects.filter(ownerID=modUser.id)
    else:
        myForums = False
        
    args = {
        'userInfo':userInfo,
        'modUser':modUser,
        'myForums': myForums,
    }
    args.update(csrf(request))
    
    return render_to_response('home.html', args)


def splash(request):
    return render_to_response('splash.html')





@login_required
def forumView(request, forumID=False):
    if not forumID:
        return redirect('/dashboard/')
    
    
    if GoogleUserInfo.objects.filter(user=request.user):
        userInfo = GoogleUserInfo.objects.get(user=request.user)
    else:
        userInfo = False
        
    
    if Forum.objects.filter(id=forumID):
        myForum = Forum.objects.get(id=forumID)
    else:
        myForum = False
        
    if ModUser.objects.filter(user=request.user):
        user = ModUser.objects.get(user=request.user)
    else:
        user = False
        
    if Post.objects.filter(text=request.user):
        text = Post.objects.get(text=request.user)
    else:
        text = False
        
    if Comment.objects.filter(text=request.user):
        text = Comment.objects.get(text=request.user)
    else:
        text = False
        
        
    args = {
        'userInfo':userInfo,
        'myForum':myForum,
        'user':user,
        'text':text,
        'comment': text,
    }
    args.update(csrf(request))
    
    return render_to_response('forum.html', args)

