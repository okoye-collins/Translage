from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, UserProfileForm
from .models import UserProfile

# Create your views here.


def signup_user(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account was successfully created')
            return redirect('login')
        
    context ={
        'form':form,
    }

    return render(request, 'accounts/signup.html', context)

@login_required
def userprofile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            valid_form = form.save(commit=False)
            valid_form.user = request.user
            valid_form.is_hausa = True if request.POST['is_hausa'] == 'on' else False
            valid_form.is_Igbo = True if request.POST['is_Igbo'] == 'on' else False
            valid_form.is_Yoruba = True if request.POST['is_Yoruba'] == 'on' else False
            valid_form.save()
            messages.success(request, "Your Profile was Succefully Updated")
            return redirect('home')
        
    context = {
        'form':form
    }
    return render(request, 'translator/userprofile.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')