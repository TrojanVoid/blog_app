from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, add_post

urlpatterns = [
    #path('posts/', add_post, name="add_post"),
    path('', HomeView.as_view(), name = 'home'),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('add_post/', add_post, name = 'add_post'),

]