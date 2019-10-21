"""recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from mainapp.views import get_index, get_add, get_index, get_signup, get_login, post_logout, post_login, post_signup
from recipes.views import get_recipe, post_create_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', get_index),
    re_path('add/(\d+)/(\d+)', get_add),
    path('index', get_index),
    path('signup', get_signup),
    path('login', get_login),
    path('login/log', post_login),
    path('logout', post_logout),
    path('signup/sign_up', post_signup),
    path('recipe', get_recipe),
    path('recipe/create', post_create_recipe),


]
