# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_index(request):

    print('test')

    return HttpResponse('Hello World')
