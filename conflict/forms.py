from django import forms
from . import models
 

class CreateArg(forms.ModelForm):
    class Meta:
        model = models.Arg
        fields = ['title', 'body', 'slug'] 

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['title', 'body', 'slug'] 