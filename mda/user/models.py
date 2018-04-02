from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

class User(AbstractUser):
    phone = models.CharField(max_length=32, unique=True)
    email = models.CharField(
        max_length=254,
        unique=True,
    )
    password = models.CharField(max_length=155)
    username = models.CharField(max_length=155, unique=False)
    REQUIRED_FIELDS = ['email', 'password']
    USERNAME_FIELD = 'phone'

    class Meta:
        db_table = "users"

class UserSeller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "sellers"

class UserBuyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.BigIntegerField(default=0)
    class Meta:
        db_table = "buyers"

