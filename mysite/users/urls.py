from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('auth-check/', views.auth_check, name='auth_check'),
]
