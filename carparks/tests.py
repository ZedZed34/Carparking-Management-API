from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CarPark


class CarParkAPITestCase(TestCase):
    def setUp(self):
        """
        Set up test data for the CarPark model.
        """
        self.client = APIClient()

        # Create sample car parks
        CarPark.objects.create(
            car_park_no="C001",
            address="BLK 308C ANG MO KIO AVENUE 1",
            x_coord=1.35735,
            y_coord=103.83783,
            car_park_type="MULTI-STOREY CAR PARK",
            type_of_parking_system="ELECTRONIC PARKING",
            short_term_parking=True,
            free_parking=True,
            night_parking=True,
            car_park_decks=5,
            gantry_height=2.1,
            car_park_basement=False,
        )
        CarPark.objects.create(
            car_park_no="C002",
            address="3 AND 7 DOVER ROAD",
            x_coord=1.30585,
            y_coord=103.77293,
            car_park_type="SURFACE CAR PARK",
            type_of_parking_system="COUPON PARKING",
            short_term_parking=False,
            free_parking=False,
            night_parking=False,
            car_park_decks=1,
            gantry_height=1.8,
            car_park_basement=False,
        )

    def test_list_carparks(self):
        """
        Test retrieving all car parks.
        """
        response = self.client.get("/api/v1/carparks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_car_park_type(self):
        """
        Test filtering car parks by type.
        """
        response = self.client.get("/api/v1/carparks/filter/", {"type": "MULTI-STOREY CAR PARK"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_free_parking(self):
        """
        Test retrieving car parks with free parking.
        """
        response = self.client.get("/api/v1/carparks/free/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_by_address(self):
        """
        Test searching for car parks by address.
        """
        response = self.client.get("/api/v1/carparks/search/", {"address": "ANG MO KIO"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_group_by_parking_system(self):
        """
        Test grouping car parks by parking system.
        """
        response = self.client.get("/api/v1/carparks/group-by-system/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        grouped_data = {entry["type_of_parking_system"]: entry["total"] for entry in response.data}
        self.assertEqual(grouped_data["ELECTRONIC PARKING"], 1)
        self.assertEqual(grouped_data["COUPON PARKING"], 1)

    def test_average_gantry_height(self):
        """
        Test retrieving the average gantry height of car parks.
        """
        response = self.client.get("/api/v1/carparks/average/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertAlmostEqual(response.data["average_height"], 1.95)

    def test_price_range_car_parks_view(self):
        """
        Test filtering car parks by gantry height range.
        """
        response = self.client.get(
            "/api/v1/carparks/height-range/", {"min_height": "1.5", "max_height": "2.0"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_car_park(self):
        """
        Test creating a new car park.
        """
        new_car_park = {
            "car_park_no": "C003",
            "address": "NEW ADDRESS",
            "x_coord": 1.30000,
            "y_coord": 103.80000,
            "car_park_type": "BASEMENT CAR PARK",
            "type_of_parking_system": "MANUAL PARKING",
            "short_term_parking": True,
            "free_parking": False,
            "night_parking": True,
            "car_park_decks": 3,
            "gantry_height": 2.5,
            "car_park_basement": True,
        }
        response = self.client.post("/api/v1/carparks/create/", new_car_park, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Duplicate creation attempt
        response = self.client.post("/api/v1/carparks/create/", new_car_park, format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_create_car_park_invalid_data(self):
        """
        Test creating a car park with invalid data.
        """
        invalid_car_park = {
            "car_park_no": "",
            "address": "",
            "gantry_height": "INVALID",
            "type_of_parking_system": "UNKNOWN",
            "free_parking": True,
        }
        response = self.client.post("/api/v1/carparks/create/", invalid_car_park, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
