from django.shortcuts import render, redirect
from .models import Recipe
from django import forms

# Create your views here.


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image_path', 'description']


def get_recipe(request):
    "Get recipe page"
    return render(request, 'recipe.html')


def post_create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

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
