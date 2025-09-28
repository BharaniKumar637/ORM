from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'fuel_type') 
    search_fields = ('brand', 'model', 'fuel_type')  
    list_filter = ('brand', 'fuel_type', 'year') 
    ordering = ('brand', 'model')  
