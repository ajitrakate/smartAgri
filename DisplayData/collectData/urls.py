from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('getData/', views.getData),
    path("change/", views.change)
]