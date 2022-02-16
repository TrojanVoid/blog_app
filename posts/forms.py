from django import forms
from .models import Post, PostView, Comment, Like

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length = 255, 
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField( required = True, widget=forms.Textarea(attrs={
                                'class': 'form-control',
                                'rows' : 5 
                                }))
    image = forms.ImageField(required = False, widget=forms.FileInput(attrs=
                                                    {'class': 'form-control-file'
                                                     }))
    

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        
"""class PostViewForm(forms.ModelForm):
    title = forms.CharField(max_length = 255, 
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField( required = True, widget=forms.Textarea(attrs={
                                'class': 'form-control',
                                'rows' : 5 
                                }))
    image = forms.ImageField(required = False, widget=forms.FileInput(attrs=
                                                    {'class': 'form-control-file'
                                                     }))
    class Meta:
        model = PostView """
        
