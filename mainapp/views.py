from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipes.models import Recipe
from django.contrib import auth
# Create your views here.


# def get_index(request):

#     print('test')

#     return HttpResponse('Hello World')


def get_add(request, a, b):
    num1 = a
    num2 = b
    result = int(num1) + int(num2)
    return HttpResponse('a + b = ' + str(result))


def get_index(request):

    text = {
        'title': 'HI~~~ this is title',
        'text': 'Here is templates'
    }

    recipes = Recipe.objects.all()
    for recipe in recipes:
        print(recipe.title)
    return render(request, 'index.html', locals())


def get_singup(request):
    return render(request, 'singup.html')


def get_login(request):

    return render(request, 'login.html')


def post_login(request):
    auth.logout(request)

    username = request.POST['username']
    password = request.POST['password']
    print('username: ' + username)
    print('password: ' + password)
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/index')
    else:
        return redirect('/index')


def post_logout(request):
    auth.logout(request)
    return redirect('/index')
