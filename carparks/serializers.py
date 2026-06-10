from rest_framework import serializers
from .models import CarPark


class CarParkSerializer(serializers.ModelSerializer):
    """
    Serializer for the CarPark model with computed fields.
    """

    has_free_parking = serializers.ReadOnlyField()
    location = serializers.ReadOnlyField()

    class Meta:
        model = CarPark
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
        # Unique enforcement handled at the view layer (IntegrityError → 409)
        # to produce a consistent response whether the collision is on the DB
        # constraint or a race condition.
        validators = []
