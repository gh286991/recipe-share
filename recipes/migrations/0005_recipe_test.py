# Generated by Django 2.2.6 on 2019-10-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_remove_recipe_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='Test',
            field=models.CharField(default='Test', max_length=100),
        ),
    ]
