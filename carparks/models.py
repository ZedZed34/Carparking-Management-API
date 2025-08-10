from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CarPark(models.Model):
    """
    Model representing a car park with all its attributes and features.
    """
    
    car_park_no = models.CharField(
        max_length=100,
        help_text="Unique identifier for the car park"
    )
    address = models.CharField(
        max_length=255,
        help_text="Full address of the car park"
    )
    x_coord = models.FloatField(
        help_text="X coordinate of the car park location"
    )
    y_coord = models.FloatField(
        help_text="Y coordinate of the car park location"
    )
    car_park_type = models.CharField(
        max_length=150,
        help_text="Type of car park (e.g., SURFACE CAR PARK, MULTI-STOREY CAR PARK)"
    )
    type_of_parking_system = models.CharField(
        max_length=150,
        help_text="Type of parking system used"
    )
    short_term_parking = models.CharField(
        max_length=100,
        help_text="Short term parking availability (e.g., WHOLE DAY, 7AM-7PM, NO)"
    )
    free_parking = models.CharField(
        max_length=100,
        help_text="Free parking availability (e.g., NO, SUN & PH FR 7AM-10.30PM)"
    )
    night_parking = models.BooleanField(
        default=False,
        help_text="Whether night parking is available"
    )
    car_park_decks = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        help_text="Number of parking decks"
    )
    gantry_height = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Height of the gantry in meters"
    )
    car_park_basement = models.BooleanField(
        default=False,
        help_text="Whether the car park has a basement"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("car_park_no", "address", "car_park_type", "gantry_height", "type_of_parking_system")
        ordering = ["address", "car_park_no"]
        verbose_name = "Car Park"
        verbose_name_plural = "Car Parks"

    def __str__(self):
        return f"Car Park {self.car_park_no} at {self.address} ({self.car_park_type})"
    
    @property
    def has_free_parking(self):
        """Returns True if the car park offers any free parking."""
        return self.free_parking.upper() not in ["NO", "FALSE"]
    
    @property
    def location(self):
        """Returns the coordinates as a tuple."""
        return (self.x_coord, self.y_coord)
