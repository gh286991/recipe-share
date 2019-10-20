from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import Recipe
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
