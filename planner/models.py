from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Wedding(models.Model):
    user = models.ForeignKey(User, null=False)
    WeddingHall = models.ForeignKey("WeddingHall")
    Car = models.ForeignKey("Car")
    Photographer = models.ForeignKey("Photographer")
    Band = models.ForeignKey("Band")
    WeddingRings = models.ForeignKey("WeddingRings")
    AlcoholBeverages = models.ForeignKey("AlcoholBeverages")
    NonAlcoholBeverages = models.ForeignKey("NonAlcoholBeverages")
    Church = models.ForeignKey("Church")
    Other = models.ForeignKey("Other")

    def __str__(self):
        return "user: {} | wedding: {}".format(self.user, self.pk)


class WeddingHall(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return "user: {} name: {}".format(self.user, self.name)


class Car(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return "user: {} name: {}".format(self.user, self.name)


class Photographer(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return "user: {} name: {}".format(self.user, self.name)


class Band(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return "user: {} name: {}".format(self.user, self.name)


class WeddingRings(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return "user: {} name: {}".format(self.user, self.name)


class AlcoholBeverages(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return "user: {} name: {}".format(self.user, self.name)


class NonAlcoholBeverages(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return "user: {} name: {}".format(self.user, self.name)


class Church(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return "user: {} name: {}".format(self.user, self.name)


class Other(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return "user: {} name: {}".format(self.user, self.name)