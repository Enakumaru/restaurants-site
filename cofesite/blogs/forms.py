from django import forms
from django.db.models.base import Model
from django.forms import widgets 
from core.models import blog
from django.http import request
class blogForm(forms.ModelForm):
    class Meta:
        model=blog
        fields=('title','header_image','title_tag','author','body','category','snippet',)
        widgets={
            'title': forms.TextInput(attrs={'placeholder':'Title','class':'form-control'}),
            'header_image': forms.FileInput(attrs={'class':'form-control','type':'file',}),
            'title_tag': forms.TextInput(attrs={'placeholder':'Title tag','class':'form-control',}),
            'author': forms.HiddenInput(attrs={'class':'form-control','value':'',}),
            'body': forms.Textarea(attrs={'value':'','class':'form-control',}),
            'category': forms.Select(attrs={'class':'form-select','aria-label':"Default select example",}),
            'snippet': forms.TextInput(attrs={'placeholder':'Add Snippet here','class':'form-control',}),
        }
#'placeholder':'Add body','aria-label':"Default select example",'disabled':'''author': forms.Select(attrs={'class':'form-control','value':'',}),
        
class EditblogForm(forms.ModelForm):
    class Meta:
        model=blog
        fields=('title','header_image','title_tag','body','category','snippet',)
        widgets={
            'title': forms.TextInput(attrs={'placeholder':'Title','class':'form-control'}),
            'header_image': forms.FileInput(attrs={'class':'form-control','type':'file',}),
            'title_tag': forms.TextInput(attrs={'placeholder':'Title tag','class':'form-control',}),
            'body': forms.Textarea(attrs={'placeholder':'Add body','class':'form-control',}),
            'category': forms.Select(attrs={'class':'form-select','aria-label':"Default select example",}),
            'snippet': forms.TextInput(attrs={'placeholder':'Add Snippet here','class':'form-control',}),
        }


