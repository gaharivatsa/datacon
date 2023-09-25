from django.urls import path
from . import views

urlpatterns = [
    path('api/getcontent', views.getcontent,name='content'),
]