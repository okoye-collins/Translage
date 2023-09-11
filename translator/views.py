from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import UserProfile
from accounts.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
import nltk
from .models import SentenceTokenize, File, Translation
import json

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

    all_translated_task = Translation.objects.filter(translator=user_profile)

    # check if the text, translated has been done for all the language selected by the translator
    xy_= {}
    TaskDoneID = []
    for task in all_translated_task:
        if task.totranslate.id in xy_:
            if task.language in xy_[task.totranslate.id]:
                xy_[task.totranslate.id][task.language] = True
            else:
                xy_[task.totranslate.id][task.language] = False
        else:
            xy_[task.totranslate.id] = {lan:False for lan in user_langauge}
            xy_[task.totranslate.id][task.language] = True

        if all(xy_[task.totranslate.id].values()):
            TaskDoneID.append(task.totranslate.id)

    all_task = SentenceTokenize.objects.all().exclude(id__in=TaskDoneID)

    data = { lan:[] for lan in user_langauge }
    for task in all_translated_task:
        task_done = {'task_id':task.id, 'task': task.totranslate.task, 'translation': task.translation}
        data[task.language].append(task_done)

    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES.get('file')
            if file is not None and file.name.endswith(".txt"):
                file_name = file.name
                uploaded_file = request.FILES['file']
                file_contents = uploaded_file.read().decode('utf-8')
                sentences = tokenize_sentences(file_contents)
                store_file = File.objects.create(file=uploaded_file)
                for sentence in sentences:
                    SentenceTokenize.objects.create(file=store_file, task=sentence) 
                return redirect('.')
            else:
                messages.error(request, "This file format is not supported")
                return redirect('.')
        else:
            # print('=================', request.POST)
            task_id = request.POST['task']
            language = request.POST['options'] 
            translation = request.POST['translation']

            try:
                Translation.objects.get(translator=user_profile, totranslate_id=int(task_id), language=language)
                messages.success(request, "You have already translated this task for the selected language.")
            except Translation.DoesNotExist:
                Translation.objects.create(translator=user_profile,totranslate_id=int(task_id), language=language, translation=translation)
                messages.success(request, "You have successfully translated the task.")
            except Translation.MultipleObjectsReturned:
                messages.error(request, "Multiple translations found for this task and language.")
            
            return redirect('.')

    user_language_json = json.dumps(user_langauge)
    context = {
        'languages': user_langauge,
        'list_lan': user_language_json,
        'all_task': all_task,
        'data': data,
    }

    
    return render(request, 'translator/home.html', context)

def post_translated_task(request):
    print('-----------', request.POST)
    return redirect('')