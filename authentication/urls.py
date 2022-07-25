from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static  

app_name = 'auth'
urlpatterns = [
    path('user/singup/', auth_signup, name="auth_signup"),
    path('user/login/', login_view, name="login_view"),
    path('user/logout/', logout_view, name="logout_view"),
    path("saveRegisterForm/", SaveRegisterForm, name="SaveRegisterForm")
]