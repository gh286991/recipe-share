from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_index(request):

    print('test')

    return HttpResponse('Hello World')


def get_add(request, a, b):
    num1 = a
    num2 = b
    result = int(num1) + int(num2)
    return HttpResponse('a + b = ' + str(result))


def get_index(request):

    texts = {
        'title': 'HI~~~ this is title',
        'text': 'Here is templates'
    }
    return render(request, 'index.html', texts)
