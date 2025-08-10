from rest_framework import serializers
from .models import CarPark


class CarParkSerializer(serializers.ModelSerializer):
    """
    Serializer for the CarPark model with custom validation and computed fields.
    """
    
    has_free_parking = serializers.ReadOnlyField()
    location = serializers.ReadOnlyField()
    
    class Meta:
        model = CarPark
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
    
    def validate_gantry_height(self, value):
        """
        Validate that gantry height is within reasonable bounds.
        """
        if value < 0:
            raise serializers.ValidationError("Gantry height cannot be negative.")
        if value > 10:
            raise serializers.ValidationError("Gantry height seems unusually high (>10m).")
        return value
    
    def validate_car_park_decks(self, value):
        """
        Validate that the number of decks is reasonable.
        """
        if value < 0:
            raise serializers.ValidationError("Number of car park decks cannot be negative.")
        if value > 50:
            raise serializers.ValidationError("Number of car park decks seems unusually high (>50).")
        return value


class CarParkListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for listing car parks with essential fields only.
    """
    
    has_free_parking = serializers.ReadOnlyField()
    
    class Meta:
        model = CarPark
        fields = [
            "id", 
            "car_park_no", 
            "address", 
            "car_park_type", 
            "gantry_height",
            "has_free_parking",
            "night_parking"
        ]


class CarParkCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new car park entries with required fields validation.
    """
    
    class Meta:
        model = CarPark
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
    
    def validate(self, data):
        """
        Validate the entire car park data for creation.
        """
        # Check if a similar car park already exists
        if CarPark.objects.filter(
            car_park_no=data.get("car_park_no"),
            address=data.get("address"),
            car_park_type=data.get("car_park_type")
        ).exists():
            raise serializers.ValidationError(
                "A car park with similar details already exists."
            )
        
        return data
