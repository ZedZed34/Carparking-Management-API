import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvancedWebDevelopment.settings")
django.setup()

from carparks.models import CarPark  # Assuming a new model for CarPark

def remove_duplicates():
    """
    Identify and remove duplicate entries in the CarPark table.
    """
    seen = set()
    duplicates = []

    for park in CarPark.objects.all():
        unique_identifier = (
            park.car_park_no,
            park.address,
            park.car_park_type,
            park.gantry_height,
            park.type_of_parking_system,
        )
        if unique_identifier in seen:
            duplicates.append(park.id)
        else:
            seen.add(unique_identifier)

    # Delete duplicates
    CarPark.objects.filter(id__in=duplicates).delete()
    print(f"Removed {len(duplicates)} duplicate entries.")


if __name__ == "__main__":
    remove_duplicates()
