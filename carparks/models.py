from django.db import models

class CarPark(models.Model):
    car_park_no = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    car_park_type = models.CharField(max_length=150)
    type_of_parking_system = models.CharField(max_length=150)
    # CSV contains values like "WHOLE DAY", "7AM-7PM", "NO" etc.
    short_term_parking = models.CharField(max_length=100)
    # CSV contains values like "NO", "SUN & PH FR 7AM-10.30PM" etc.
    free_parking = models.CharField(max_length=100)
    night_parking = models.BooleanField()
    car_park_decks = models.IntegerField()
    gantry_height = models.FloatField()
    car_park_basement = models.BooleanField()

    class Meta:
        unique_together = ("car_park_no","address", "car_park_type", "gantry_height", "type_of_parking_system")

    def __str__(self):
        return f"Car Park at {self.address} ({self.car_park_type})"
