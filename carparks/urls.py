from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.generic import RedirectView

from carparks.views import (
    # API views
    CarParkListView,
    FilteredCarParksView,
    FreeParkingView,
    GroupByParkingSystemView,
    AverageGantryHeightView,
    CarParkCreateView,
    SearchCarParksByAddressView,
    CarParkTypesView,
    CarParkDetailView,
    HeightRangeCarParksView,
    # HTML views (function-based)
    FilteredCarParksHTMLView,
    FilteredFreeParkingHTMLView,
    home_view,
    carpark_create_view,
    carpark_search_view,
    average_gantry_height_view,
    group_by_parking_system_view,
    carparks_list_view,
)

# Health check endpoint
def healthz(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),

    # Health check endpoint
    path("healthz/", healthz, name="healthz"),

    # Root → redirect to home page
    path("", RedirectView.as_view(pattern_name="home", permanent=False), name="root"),

    # Friendly prefixes under /carparks/
    path("carparks/", RedirectView.as_view(pattern_name="home", permanent=False), name="carparks-root"),
    path("carparks/list/", RedirectView.as_view(pattern_name="carparks-list", permanent=False), name="carparks-list-redirect"),
    path("carparks/create/", RedirectView.as_view(pattern_name="create-carpark-html", permanent=False), name="carparks-create-redirect"),
    path("carparks/filter-by-type/", RedirectView.as_view(pattern_name="filter-by-type", permanent=False), name="carparks-filter-by-type-redirect"),
    path("carparks/filter-free-parking/", RedirectView.as_view(pattern_name="filter-free-parking", permanent=False), name="carparks-filter-free-parking-redirect"),
    path("carparks/group-by-system/", RedirectView.as_view(pattern_name="group-by-parking-system", permanent=False), name="carparks-group-by-system-redirect"),
    path("carparks/average-height/", RedirectView.as_view(pattern_name="average-gantry-height", permanent=False), name="carparks-average-height-redirect"),
    path("carparks/search/", RedirectView.as_view(pattern_name="search-carpark", permanent=False), name="carparks-search-redirect"),

    # API v1 routes
    path("api/v1/carparks/", CarParkListView.as_view(), name="carpark-list"),
    path("api/v1/carparks/types/", CarParkTypesView.as_view(), name="carpark-types"),
    path("api/v1/carparks/<int:pk>/", CarParkDetailView.as_view(), name="carpark-detail"),
    path("api/v1/carparks/height-range/", HeightRangeCarParksView.as_view(), name="height-range"),
    path("api/v1/carparks/filter/", FilteredCarParksView.as_view(), name="filtered-carparks"),
    path("api/v1/carparks/free/", FreeParkingView.as_view(), name="free-parking"),
    path("api/v1/carparks/free-parking/", FreeParkingView.as_view(), name="free-parking-alias"),
    path("api/v1/carparks/group/", GroupByParkingSystemView.as_view(), name="group-by-parking-system"),
    path("api/v1/carparks/group-by-system/", GroupByParkingSystemView.as_view(), name="group-by-parking-system-alias"),
    path("api/v1/carparks/average/", AverageGantryHeightView.as_view(), name="average-gantry-height"),
    path("api/v1/carparks/average-gantry-height/", AverageGantryHeightView.as_view(), name="average-gantry-height-alias"),
    path("api/v1/carparks/create/", CarParkCreateView.as_view(), name="create-carpark-api"),
    path("api/v1/carparks/search/", SearchCarParksByAddressView.as_view(), name="search-carparks"),

    # HTML Views
    path("home/", home_view, name="home"),
    path("list/", carparks_list_view, name="carparks-list"),
    path("create/", carpark_create_view, name="create-carpark-html"),
    path("search/", carpark_search_view, name="search-carpark"),
    path("average-height/", average_gantry_height_view, name="average-gantry-height"),
    path("group-by-system/", group_by_parking_system_view, name="group-by-parking-system"),

    # Function-based HTML views
    path("filter-by-type/", FilteredCarParksHTMLView, name="filter-by-type"),
    path("filter-free-parking/", FilteredFreeParkingHTMLView, name="filter-free-parking"),
]
