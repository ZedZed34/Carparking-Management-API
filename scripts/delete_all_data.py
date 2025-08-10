import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvancedWebDevelopment.settings")
django.setup()

from carparks.models import CarPark  # Using the CarPark model instead of ResaleFlat

def delete_all_data():
    """
    Delete all dataset from the CarPark model.
    """
    count = CarPark.objects.count()
    CarPark.objects.all().delete()
    print(f"Deleted {count} car park records from the database.")


if __name__ == "__main__":
    print("Starting dataset deletion...")
    delete_all_data()
