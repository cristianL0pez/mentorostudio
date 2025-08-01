from django.urls import path
from . import views

urlpatterns = [
    path('', views.code_server, name='code_server'),
]
