from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class WeddingHall(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField()
    to_pay = models.FloatField(null=False)
    paid = models.FloatField()
    done = models.BooleanField()


class Car(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField()
    to_pay = models.FloatField()
    paid = models.FloatField()
    done = models.BooleanField()


class Photographer(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField()
    to_pay = models.FloatField()
    paid = models.FloatField()
    done = models.BooleanField()


class Band(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField()
    to_pay = models.FloatField()
    paid = models.FloatField()
    done = models.BooleanField()


class WeddingRings(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField()
    to_pay = models.FloatField()
    paid = models.FloatField()
    done = models.BooleanField()