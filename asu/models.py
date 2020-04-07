from django.db import models

class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Group:
    name = models.CharField(max_length=30)

class Lesson:

# Create your models here.
