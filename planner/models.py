from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Wedding(models.Model):
    user = models.OneToOneField(User, null=False)

    def __str__(self):
        return "{}".format(self.user.pk)


class WeddingHall(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)
    wedding = models.ForeignKey(Wedding, null=False)

    def __str__(self):
        return "wedding: {} name: {}".format(self.wedding, self.name)


class Car(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)
    wedding = models.ForeignKey(Wedding, null=False)

    def __str__(self):
        return "wedding: {} name: {}".format(self.wedding, self.name)


class Photographer(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)
    wedding = models.ForeignKey(Wedding, null=False)

    def __str__(self):
        return "wedding: {} name: {}".format(self.wedding, self.name)


class Band(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)
    wedding = models.ForeignKey(Wedding, null=False)

    def __str__(self):
        return "wedding: {} name: {}".format(self.wedding, self.name)


class WeddingRings(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)
    wedding = models.ForeignKey(Wedding, null=False)

    def __str__(self):
        return "wedding: {} name: {}".format(self.wedding, self.name)


class AlcoholBeverages(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)
    wedding = models.ForeignKey(Wedding, null=False)

    def __str__(self):
        return "wedding: {} name: {}".format(self.wedding, self.name)


class NonAlcoholBeverages(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)
    wedding = models.ForeignKey(Wedding, null=False)

    def __str__(self):
        return "wedding: {} name: {}".format(self.wedding, self.name)


class Church(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)
    wedding = models.ForeignKey(Wedding, null=False)

    def __str__(self):
        return "wedding: {} name: {}".format(self.wedding, self.name)


class Other(models.Model):
    name = models.CharField(max_length=256)
    cost = models.FloatField(null=True)
    to_pay = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    done = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False)
    wedding = models.ForeignKey(Wedding, null=False)

    def __str__(self):
        return "wedding: {} name: {}".format(self.wedding, self.name)