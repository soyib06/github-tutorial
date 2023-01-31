from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from . import forms
# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        form = forms.SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store')
    form = forms.SignInForm()
    return render(request, 'store/sign_in.html', {'form': form})    

def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sign_in')
    form = forms.SignUpForm()
    return render(request, 'store/sign_up.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('sign_in')

def edit_profile(request):
    form = forms.EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('profile_list')
    form = forms.EditProfileForm(instance=request.user)
    return render(request, 'store/edit_profile.html', {'form':form}) 

def reset_password(request):
    form = forms.ChangePasswordForm(request.user, request.POST)
    if request.method == 'POST' and form.is_valid(): 
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('sign_in')
    form = forms.ChangePasswordForm(request.user)
    return render(request, 'store/reset_password.html', {'form': form})
