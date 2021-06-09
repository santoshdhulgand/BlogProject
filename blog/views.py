from blog.models import Post
from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User


from django.views.generic import (
    TemplateView ,
    ListView ,
    DetailView ,
    CreateView ,
    UpdateView , 
    DeleteView
)


class IndexPageView(TemplateView):
    template_name = 'blog/index.html'



class PostListView(LoginRequiredMixin , ListView):
    model               = Post
    template_name       = 'blog/home.html' # <app_name>/<model>_<view_type>.html
    context_object_name = 'posts' 
    ordering            = ['-date_posted']
    paginate_by         = 2


class UserPostListView(LoginRequiredMixin , ListView):
    model               = Post
    template_name       = 'blog/user_post.html' # <app_name>/<model>_<view_type>.html
    context_object_name = 'posts' 
    
    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin , DetailView):
    model = Post


class PostCreateView(CreateView):
    model           = Post
    template_name   = 'blog/new.html'
    fields          = ['title' , 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin , UpdateView):
    model           = Post
    template_name   = 'blog/update.html'
    fields          = ['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin , DeleteView):
    model           = Post
    template_name   = 'blog/delete.html'
    success_url     = reverse_lazy('blog-posts')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


