
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, 
                               required=True, 
                               widget=forms.TextInput(attrs=
                                                      {'class': 'form-control',
                                                       'placeholder': 'Username'}
                                                      ))
    password = forms.CharField( max_length=30, 
                               required=True, 
                               widget=forms.PasswordInput(attrs=
                                                          {'class': 'form-control', 
                                                           'placeholder': 'Password',
                                                           'data-toggle': 'password',
                                                           'id': 'password',
                                                           'name' : 'password'
                                                           }))
    
    class Meta:
        model = User
        fields = ['username', 'password']
    
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email']
        
class UserProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(required = False, widget=forms.FileInput(attrs=
                                                    {'class': 'form-control-file'
                                                     }))
    bio = forms.CharField(widget=forms.Textarea(attrs=
                                                {
                                                    'class' : 'form-control',
                                                    'rows' : 5
                                                }))
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'bio']