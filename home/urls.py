from django.contrib import admin
from django.urls import path, include
from .views import *
app_name = 'home'
urlpatterns = [
    path('', home_index, name="home_index"),
    path('dashboard/<str:type>', dashboard, name="dashboard")
]