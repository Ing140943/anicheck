from django import forms

from blog.models.blog import Review

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
