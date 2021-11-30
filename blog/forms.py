from django import forms

from blog.models.blog import Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CharFieldForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'body']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Review title'}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                                       'placeholder': 'Description...'}),
        }

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
