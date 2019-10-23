from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Recipe
from django import forms
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
import json


# Create your views here.


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image_path', 'description', 'author']


def get_recipe(request):
    "Get recipe page"
    return render(request, 'recipe.html')


def post_create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        print(request.POST)
        user = request.user
        print(user.username)

        if form.is_valid():
            form.save()
            # print('新增的recipe: ' + new_recipe)
            return redirect('/index')
        else:
            return redirect('/recipe')


def post_delete_recipe(request):
    print('Delte!!!!!')
    ID = request.POST['cId']  # 取得表單輸入的編號
    recipe = Recipe.objects.get(pk=ID)
    recipe.delete()  # 刪除資料

    return redirect('/index')


def get_update(request):
    ID = request.POST['cId']
    recipe = Recipe.objects.get(pk=ID)
    return render(request, 'update.html', locals())


def post_update_recipe(request):
    print('Update-----')
    ID = request.POST['cId']  # 取得表單輸入的編號
    recipe = Recipe.objects.get(pk=ID)
    recipes = serialize('json', Recipe.objects.all(), ensure_ascii=False)
    print(recipes)

    form = RecipeForm(request.POST or None, instance=recipe)

    if form.is_valid():
        form.save()
        return redirect('/index')

    return redirect('/recipe/update')
