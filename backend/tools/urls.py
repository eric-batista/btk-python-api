
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='Tools homepage'),
    path('markowitz/', views.MarkowitzView.as_view(), name='Tools Markowitz')
]
