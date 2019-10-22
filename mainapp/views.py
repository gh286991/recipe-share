from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from recipes.models import Recipe

# Create your views here.


def get_add(request, A, B):
    "This get the sum of A & B"
    num1 = A
    num2 = B
    result = int(num1) + int(num2)
    return HttpResponse('a + b = ' + str(result))


def get_index(request):
    "This get index page"

    recipes = Recipe.objects.all()

    return render(request, 'index.html', locals())


def get_signup(request):
    "This get the sign up page"
    return render(request, 'signup.html')


def get_login(request):
    "This get the log in page"
    return render(request, 'login.html')


def post_login(request):
    "This is post log in data"
    auth.logout(request)

    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/index')
    else:
        return redirect('/index')


def post_logout(request):
    "loguou function"
    auth.logout(request)
    return redirect('/index')


def post_signup(request):
    "post signup request"
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    User = auth.models.User
    user = User.objects.create_user(username, email, password)

    if user:
        userlogin = auth.authenticate(username=username, password=password)
        auth.login(request, userlogin)
        return redirect('/index', locals())
    else:
        redirect('/signup', locals())
