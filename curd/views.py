from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpRequest
from django.utils import timezone
from django.contrib import messages
from .models import Post

def dashboard(request):
    posts = Post.objects.order_by("-created_at")[:5]
    context = {
        "posts": posts,
    }
    return render(request, "curd/dashboard.html",context)

def edit(request,id):
    posts = Post.objects.order_by("-created_at")[:5]
    edit_post = Post.objects.get(id=id)
    context = {
        "posts": posts,
        'edit_post':edit_post
    }
    return render(request, "curd/edit.html",context)

def curd_submit(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        post = Post.objects.create(
            name=name,
            email=email,
            created_at=timezone.now()
            )
    
        post.save()
        messages.success(request, 'Post added successfully.')
        return redirect('curd:dashboard')
    else:
        return redirect('dashboard')

def edit_submit(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        post =Post.objects.get(id=id)
        post.name=name
        post.email=email
        post.save()
        messages.success(request, 'Post '+str(id)+' edited successfully.')
        return redirect('curd:dashboard')
    else:
        return redirect('dashboard')

def curd_delete(request,id):
    Post.objects.filter(id=id).delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('curd:dashboard')
