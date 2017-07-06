from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(AppUser)
class AdminAppUser(admin.ModelAdmin):
    pass


@admin.register(WeddingHall)
class AdminWeddingHallr(admin.ModelAdmin):
    pass


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    pass


@admin.register(Photographer)
class AdminPhotographer(admin.ModelAdmin):
    pass


@admin.register(Band)
class AdminBand(admin.ModelAdmin):
    pass


@admin.register(WeddingRings)
class AdminWeddingRings(admin.ModelAdmin):
    pass