from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login_user, name='login'),
    path('post_translated_task', views.post_translated_task, name='post_translated_task'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('download/<str:file_name>/', views.download_translation, name='download_txt_file'),
    path('rate_task/', views.rate_task, name='rate_task'),
    


]