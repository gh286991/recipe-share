# Generated by Django 2.2.6 on 2019-10-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]
