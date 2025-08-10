import os
import sys
import django
import pandas as pd

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvancedWebDevelopment.settings")
django.setup()

from carparks.models import CarPark  # Import the CarPark model

def load_data_from_csv(file_path):
    """
    Load dataset from a CSV file into the database, skipping duplicates
    and reporting the number of duplicates skipped.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # Load the CSV file
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return

    # Required columns
    # Align with CSV headers
    required_columns = [
        "car_park_no",
        "address",
        "x_coord",
        "y_coord",
        "car_park_type",
        "type_of_parking_system",
        "short_term_parking",
        "free_parking",
        "night_parking",
        "car_park_decks",
        "gantry_height",
        "car_park_basement",
    ]

    # Check for missing columns
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"Error: Missing required columns in CSV: {', '.join(missing_columns)}")
        return

    duplicates_count = 0
    inserted_count = 0

    for _, row in data.iterrows():
        # Check if the record already exists
        if CarPark.objects.filter(
            car_park_no=row["car_park_no"],
            address=row["address"],
            car_park_type=row["car_park_type"],
            gantry_height=float(row["gantry_height"]),
            type_of_parking_system=row["type_of_parking_system"],
        ).exists():
            duplicates_count += 1
            continue

        # Insert new record
        CarPark.objects.create(
            car_park_no=row["car_park_no"],
            address=row["address"],
            x_coord=float(row["x_coord"]),
            y_coord=float(row["y_coord"]),
            car_park_type=row["car_park_type"],
            type_of_parking_system=row["type_of_parking_system"],
            short_term_parking=row["short_term_parking"],
            free_parking=row["free_parking"],
            night_parking=True if str(row["night_parking"]).strip().upper() in ["Y", "YES", "TRUE", "T", "1"] else False,
            car_park_decks=int(row["car_park_decks"]),
            gantry_height=float(row["gantry_height"]),
            car_park_basement=True if str(row["car_park_basement"]).strip().upper() in ["Y", "YES", "TRUE", "T", "1"] else False,
        )
        inserted_count += 1

    print(
        f"Data loading completed. {inserted_count} records inserted, {duplicates_count} duplicates skipped."
    )


if __name__ == "__main__":
    # Path to the CSV file
    file_path = os.path.join(os.path.dirname(__file__), "../dataset/HDBCarparkInformation.csv")

    # Load dataset from CSV into the database
    print("Loading dataset from CSV...")
    load_data_from_csv(file_path)