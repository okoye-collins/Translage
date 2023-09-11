from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login_user, name='login'),
    path('post_translated_task', views.post_translated_task, name='post_translated_task'),


]