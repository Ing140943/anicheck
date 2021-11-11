# from django import forms

# class CharFieldForm(forms.Form):
#     memo = forms.CharField(
#         label='',
#         required=False,
#         max_length = 150,
#         widget=forms.Textarea(attrs={
#             'placeholder': 'write your comment',
#             'cols': '40',
#             'rows': '3'
#         })
#     )

from django.forms import ModelForm, Textarea
from models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }