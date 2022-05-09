from django.contrib import admin
from .models import Snacks

@admin.register(Snacks)
class AdminSnacks(admin.ModelAdmin):
    pass