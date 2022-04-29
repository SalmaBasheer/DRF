from atexit import register
from unicodedata import name
from django import views
from django.db import router
from .views import RegisterAPI, LoginAPI,BlogpostListApiView
# from rest_framework import routers,viewsets
from knox import views as knox_views
from django.urls import path,include



urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/Blogpost',BlogpostListApiView.as_view())
    ]
    
