from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment
from taggit.forms import TagWidget # type: ignore # Import TagWidget for styling the tag input field

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # Use TagWidget for a better tag input experience
        }

        def clean_tags(self):
         tags = self.cleaned_data['tags']
         return [tag.strip() for tag in tags.split(",")]  # Convert input into list

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Adding an email field

    class Meta:
        model = User
        fields =  ['username', 'email', 'password1', 'password2']  # Custom fields

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] # Allows users to update their username and email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio'] # Allows users to update their profile picture and bio

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Ensures only content is editable

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 3:
            raise forms.ValidationError("Comment must be at least 3 characters long.")
        return content
