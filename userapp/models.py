from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    ism = models.CharField(max_length=60)
    email = models.EmailField(max_length=200)
    jins = models.CharField(max_length=30, choices=[("Erkak", "Erkak"), ("Ayol", "Ayol")])
    shahar = models.CharField(max_length=40)
    mamlakat = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism
