from django.contrib import admin
from .models import CarPark  # Update to CarPark


# Register your models here.
@admin.register(CarPark)
class CarParkAdmin(admin.ModelAdmin):
    list_display = ("address", "car_park_type", "gantry_height", "type_of_parking_system", "free_parking")
    search_fields = ("address", "car_park_type", "type_of_parking_system")