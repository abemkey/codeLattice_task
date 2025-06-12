from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    age = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):
        return self.name