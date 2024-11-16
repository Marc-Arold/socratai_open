from django.contrib import admin
from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
    
    path('', views.renderchat, name='chat'),
    path('message/', views.conversation, name='message'),
    path('feebback/', views.feedback, name='feedback'),
]
