from django.db import models
from django.contrib.auth.models import AbstractUser


class ChefCuisineModel(AbstractUser):
    CREATOR = 'Créateur'
    SUBSCRIBER = 'Abonné'
    CHOICES = [
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné')
    ]
    role = models.CharField(max_length = 50, choices=CHOICES)
    speciality_food = models.CharField(max_length=50)
