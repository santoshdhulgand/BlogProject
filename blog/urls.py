

from django.urls import path
from blog import views

urlpatterns = [
     path('index/' , views.IndexPageView.as_view()),
     path('' , views.PostListView.as_view() , name = 'blog-posts'),
     path('post/user/<username>/' , views.UserPostListView.as_view() , name = 'user-posts'),
     path('post/<int:pk>/' , views.PostDetailView.as_view() , name = 'post-detail'),
     path('post/update/<int:pk>/' , views.PostUpdateView.as_view() , name = 'post-update'),
     path('post/delete/<int:pk>/' , views.PostDeleteView.as_view() , name = 'post-delete'),
     path('post/new/' , views.PostCreateView.as_view() , name = 'post-create'),


]
