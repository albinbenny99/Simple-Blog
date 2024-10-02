from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, UserProfileForm
from .models import BlogPost

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

def index(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})
from django.shortcuts import get_object_or_404
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django import forms

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags']

@login_required
def new_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_post', id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'delete_post.html', {'post': post})

def view_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'view_post.html', {'post': post})
