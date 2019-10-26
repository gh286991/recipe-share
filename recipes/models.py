from django.db import models
from django.utils import timezone

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    Test = models.CharField(default="Test", max_length=100)
    create_data = models.DateTimeField(auto_now_add=True, blank=True)
