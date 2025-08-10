from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Count
from django.shortcuts import render
from .models import CarPark
from .serializers import CarParkSerializer
from django.http import HttpResponse
from uuid import uuid4
from django.shortcuts import get_object_or_404

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
        # In CSV, free_parking is textual. Treat anything other than explicit 'NO' as free option available
        car_parks = CarPark.objects.exclude(free_parking__iexact="NO")
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
        # Accept minimal payload and fill sensible defaults for required fields
        payload = request.data.copy()
        payload.setdefault("car_park_no", f"MANUAL-{uuid4().hex[:8].upper()}")
        payload.setdefault("x_coord", 0)
        payload.setdefault("y_coord", 0)
        payload.setdefault("type_of_parking_system", "ELECTRONIC PARKING")
        payload.setdefault("short_term_parking", "NO")
        payload.setdefault("free_parking", "NO")
        payload.setdefault("night_parking", False)
        payload.setdefault("car_park_decks", 0)
        payload.setdefault("gantry_height", 0)
        payload.setdefault("car_park_basement", False)

        serializer = CarParkSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Feature 7: Search Car Parks by Address
class SearchCarParksByAddressView(APIView):
    def get(self, request):
        address_query = request.query_params.get('address', None)
        if address_query:
            car_parks = CarPark.objects.filter(address__icontains=address_query)
            serializer = CarParkSerializer(car_parks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Address query not specified"}, status=status.HTTP_400_BAD_REQUEST)

# HTML Views
def home_view(request):
    return render(request, "carparks/home.html")

def carpark_create_view(request):
    return render(request, "carparks/create.html")

def carpark_search_view(request):
    return render(request, "carparks/search.html")

def average_gantry_height_view(request):
    return render(request, "carparks/average_gantry_height.html")

def group_by_parking_system_view(request):
    return render(request, "carparks/group_by_parking_system.html")

def FilteredCarParksHTMLView(request):
    return render(request, "carparks/filter_by_type.html")

def FilteredFreeParkingHTMLView(request):
    return render(request, "carparks/filter_free_parking.html")

# New: distinct car park types API for populating dropdowns
class CarParkTypesView(APIView):
    def get(self, request):
        types = list(
            CarPark.objects.values_list("car_park_type", flat=True).distinct().order_by("car_park_type")
        )
        return Response(types, status=status.HTTP_200_OK)

# New: All car parks HTML list page
def carparks_list_view(request):
    return render(request, "carparks/list.html")

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
