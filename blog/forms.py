from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import BlogPost


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags']
        
    # Optional: You can add custom validation or widgets if needed
    # Example of adding placeholder text
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Enter post title'})
        self.fields['content'].widget.attrs.update({'placeholder': 'Write your content here'})
        self.fields['tags'].widget.attrs.update({'placeholder': 'Add tags separated by commas'})