from django.db import models


class Recipe(models.Model):
    creator = models.CharField(max_length=50)
    steps = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
