from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserForm, UserProfileForm

from django.contrib import messages

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render(request, 'users/base.html')

@csrf_exempt
def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
    
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                messages.success(request, 'Login successful!')
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Account is not active')
                return render(request, 'login.html', {'form' : form})
        else:
            messages.error(request, 'Username or password is wrong!')
            return render(request, 'login.html', {'form' : form})
    
    return render(request, 'registration/login.html', {'form' : form})

def user_logout(request):
    logout(request)

def user_register(request):
    
    form_user = UserForm(request.POST or None)
    form_profile = UserProfileForm(request.POST or None)
    if form_user.is_valid() and form_profile.is_valid():
        user = form_user.save()
        profile = form_profile.save(commit = False)
        profile.user = user
    
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        return redirect('index')
        
    context = {
        'form_user' : form_user,
        'form_profile' : form_profile,
    }
    
    return render(request, 'registration/register.html', context)

@csrf_exempt
@login_required 
def user_profile(request): 
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully.')
            return redirect(to='user_profile')
    else: 
        user_form = UserForm(instance = request.user)
        profile_form = UserProfileForm(instance = request.user.userprofile)
            
    return render(request, 'users/user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form        
    })
    
class change_password(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = 'You have successfully changed your password'
    success_url = reverse_lazy('index')

