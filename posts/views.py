from django.shortcuts import render, redirect
# from .forms import PostForm, PostViewForm
from .models import Post

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm

from django.contrib.auth.models import User

""" def add_post(request):
    form_post = PostForm(request.POST or None)
    form_post_view = PostViewForm(request.POST or None)
    
    if form_post.is_valid():
        post = form_post.save()
        post_view = form_post_view.save()
        post_view.post = post
        
        if 'image' in request.FILES:
            post_view.image = request.FILES['image']
        
        post_view.save()
        return redirect('index')
    context = {
        'form_post' : form_post,
        'form_post_view' : form_post_view
    }
        
    return render(request, 'base.html')
 """
class HomeView(ListView):
    model = Post
    template_name = 'posts/home.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    
    
def add_post(request):
    form_post = PostForm(request.POST or None)
    
    if form_post.is_valid() and request.user.is_authenticated:
        post = form_post.save(commit=False)
        post.user = User.objects.get(pk=request.user.id)
        
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post = form_post.save()
            
        return redirect('home')
    context = {
        'form' : form_post,
    }
        
    return render(request, 'posts/add_post.html', context)
    
class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/add_post.html'
    fields = '__all__'