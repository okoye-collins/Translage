from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import UserProfile
from accounts.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
import nltk
from .models import SentenceTokenize, File

# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user)
        if request.user.is_superuser:
            return redirect('../admin')
        elif user_profile.exists():
            return redirect('home')
        else:
            return redirect('userprofile')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # check if the user exist
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                userprofile =UserProfile.objects.filter(user=user)
                if userprofile.exists():
                    return redirect('home')
                else:
                    return redirect('userprofile')
            else:
                messages.error(request, "Invalid email or password.")
            
    context ={
        'form':form
    }

    return render(request, 'accounts/login.html', context)

def tokenize_sentences(file_contents):
    sentences = nltk.sent_tokenize(file_contents)
    return sentences

@login_required
def home(request):
    user = request.user
    user_langauge = []
    user_profile = UserProfile.objects.filter(user=user).first()
    if user_profile.is_hausa:
        user_langauge.append('Hausa')
    if user_profile.is_Igbo:
        user_langauge.append('Igbo')
    if user_profile.is_Yoruba:
        user_langauge.append('Yoruba')
    context = {}
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES.get('file')
        if file is not None and file.name.endswith(".txt"):
            file_name = file.name
            uploaded_file = request.FILES['file']
            file_contents = uploaded_file.read().decode('utf-8')
            sentences = tokenize_sentences(file_contents)
            store_file = File.objects.create(file=uploaded_file)
            store_sentences_tokenize = SentenceTokenize.objects.create(file=store_file, task=sentences)
            context['sentences'] = sentences
            print('File name:', file_name)
        else:
            print('--------This file format is not supported')
            messages.error(request, "This file format is not supported")
    
    context['languages']= user_langauge
    
    return render(request, 'translator/home.html', context)