from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Count
from .models import CarPark
from .serializers import CarParkSerializer
from uuid import uuid4
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

_BOOL_TO_TEXT = {True: "TRUE", False: "FALSE"}


def _to_text(val):
    """Convert Python booleans to 'TRUE'/'FALSE', pass everything else through."""
    return _BOOL_TO_TEXT.get(val, val)

# Feature 1: View All Car Parks
class CarParkListView(APIView):
    def get(self, request):
        car_parks = CarPark.objects.all()
        serializer = CarParkSerializer(car_parks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Feature 2: Filter by Car Park Type
class FilteredCarParksView(APIView):
    def get(self, request):
        car_park_type = request.query_params.get('type', None)
        if car_park_type:
            car_parks = CarPark.objects.filter(car_park_type__iexact=car_park_type)
            serializer = CarParkSerializer(car_parks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Car park type not specified"}, status=status.HTTP_400_BAD_REQUEST)

# Feature 3: Filter Free Parking
class FreeParkingView(APIView):
    def get(self, request):
        # Treat explicit 'NO' or 'FALSE' as not free; everything else is free
        car_parks = CarPark.objects.exclude(free_parking__iexact="NO").exclude(free_parking__iexact="FALSE")
        serializer = CarParkSerializer(car_parks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Feature 4: Group by Parking System
class GroupByParkingSystemView(APIView):
    def get(self, request):
        grouped_data = CarPark.objects.values('type_of_parking_system').annotate(total=Count('id'))
        return Response(grouped_data, status=status.HTTP_200_OK)

# Feature 5: Average Gantry Height
class AverageGantryHeightView(APIView):
    def get(self, request):
        average_height = CarPark.objects.aggregate(average_height=Avg('gantry_height'))
        return Response(average_height, status=status.HTTP_200_OK)

# Feature 6: Add New Car Park
class CarParkCreateView(APIView):
    def post(self, request):
        payload = request.data.copy()
        payload.setdefault("car_park_no", f"MANUAL-{uuid4().hex[:8].upper()}")
        payload.setdefault("x_coord", 0)
        payload.setdefault("y_coord", 0)
        payload.setdefault("type_of_parking_system", "ELECTRONIC PARKING")

        # Normalize booleans for CharFields
        payload["short_term_parking"] = _to_text(payload.get("short_term_parking", "NO"))
        payload["free_parking"] = _to_text(payload.get("free_parking", "NO"))
        payload.setdefault("night_parking", False)
        payload.setdefault("car_park_decks", 0)
        payload.setdefault("gantry_height", 0)
        payload.setdefault("car_park_basement", False)

        # Validate then save; DB unique_together constraint catches duplicates
        serializer = CarParkSerializer(data=payload)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = serializer.save()
        except IntegrityError:
            return Response({"detail": "Duplicate car park"}, status=status.HTTP_409_CONFLICT)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# New: filter by gantry height range
class HeightRangeCarParksView(APIView):
    def get(self, request):
        min_h = request.query_params.get("min_height")
        max_h = request.query_params.get("max_height")
        if min_h is None or max_h is None:
            return Response({"error": "min_height and max_height are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            min_v = float(min_h)
            max_v = float(max_h)
        except ValueError:
            return Response({"error": "Invalid height values"}, status=status.HTTP_400_BAD_REQUEST)
        car_parks = CarPark.objects.filter(gantry_height__gte=min_v, gantry_height__lte=max_v)
        return Response(CarParkSerializer(car_parks, many=True).data, status=status.HTTP_200_OK)

# Feature 7: Search Car Parks by Address
class SearchCarParksByAddressView(APIView):
    def get(self, request):
        address_query = request.query_params.get('address', None)
        if address_query:
            car_parks = CarPark.objects.filter(address__icontains=address_query)
            serializer = CarParkSerializer(car_parks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Address query not specified"}, status=status.HTTP_400_BAD_REQUEST)


# New: distinct car park types API for populating dropdowns
class CarParkTypesView(APIView):
    def get(self, request):
        types = list(
            CarPark.objects.values_list("car_park_type", flat=True).distinct().order_by("car_park_type")
        )
        return Response(types, status=status.HTTP_200_OK)

# New: retrieve/update/delete a single car park
class CarParkDetailView(APIView):
    def get(self, request, pk: int):
        car_park = get_object_or_404(CarPark, pk=pk)
        return Response(CarParkSerializer(car_park).data, status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        car_park = get_object_or_404(CarPark, pk=pk)
        serializer = CarParkSerializer(car_park, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int):
        car_park = get_object_or_404(CarPark, pk=pk)
        serializer = CarParkSerializer(car_park, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
