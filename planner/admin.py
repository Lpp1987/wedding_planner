from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Wedding)
class AdminWedding(admin.ModelAdmin):
    pass