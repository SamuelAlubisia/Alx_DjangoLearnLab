from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import your custom views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView
     
)
from .views import search_posts
from .views import PostByTagListView  


urlpatterns = [
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="add-comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="edit-comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"),
]

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
]


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='blog-home'),  # Home page for the blog app
]

urlpatterns = [
    path('search/', search_posts, name='search'),
    path('tags/<str:tag_name>/', PostsByTagView.as_view(), name='posts_by_tag'), # type: ignore
]

urlpatterns = [
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]
