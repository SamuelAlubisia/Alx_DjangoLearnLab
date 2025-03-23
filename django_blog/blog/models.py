from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User 
from taggit.managers import TaggableManager # type: ignore

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default="No content provided")
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'posts' )
    tags = TaggableManager()  # Enables tagging

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/posts/{self.id}/"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default="No content provided")
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set when comment is created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on each save
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'