from django.urls import path
from django.views.generic import RedirectView, TemplateView

from carparks.views import (
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
)


_REDIRECTS = {
    "": ("home", "root"),
    "carparks/": ("home", "carparks-root"),
    "carparks/list/": ("carparks-list", "carparks-list-redirect"),
    "carparks/create/": ("create-carpark-html", "carparks-create-redirect"),
    "carparks/filter-by-type/": ("filter-by-type", "carparks-filter-by-type-redirect"),
    "carparks/filter-free-parking/": ("filter-free-parking", "carparks-filter-free-parking-redirect"),
    "carparks/group-by-system/": ("group-by-parking-system", "carparks-group-by-system-redirect"),
    "carparks/average-height/": ("average-gantry-height", "carparks-average-height-redirect"),
    "carparks/search/": ("search-carpark", "carparks-search-redirect"),
}

urlpatterns = [
    # Note: admin and health endpoints are defined in project urls

    # Friendly prefixes under /carparks/
    *(
        path(prefix, RedirectView.as_view(pattern_name=pname, permanent=False), name=name)
        for prefix, (pname, name) in _REDIRECTS.items()
    ),

    # API v1 routes
    path("api/v1/carparks/", CarParkListView.as_view(), name="carpark-list"),
    path("api/v1/carparks/types/", CarParkTypesView.as_view(), name="carpark-types"),
    path("api/v1/carparks/<int:pk>/", CarParkDetailView.as_view(), name="carpark-detail"),
    path("api/v1/carparks/height-range/", HeightRangeCarParksView.as_view(), name="height-range"),
    path("api/v1/carparks/filter/", FilteredCarParksView.as_view(), name="filtered-carparks"),
    path("api/v1/carparks/free-parking/", FreeParkingView.as_view(), name="free-parking"),
    path("api/v1/carparks/group-by-system/", GroupByParkingSystemView.as_view(), name="group-by-parking-system"),
    path("api/v1/carparks/average-gantry-height/", AverageGantryHeightView.as_view(), name="average-gantry-height"),
    path("api/v1/carparks/create/", CarParkCreateView.as_view(), name="create-carpark-api"),
    path("api/v1/carparks/search/", SearchCarParksByAddressView.as_view(), name="search-carparks"),

    # HTML Views
    path("home/", TemplateView.as_view(template_name="carparks/home.html"), name="home"),
    path("list/", TemplateView.as_view(template_name="carparks/list.html"), name="carparks-list"),
    path("create/", TemplateView.as_view(template_name="carparks/create.html"), name="create-carpark-html"),
    path("search/", TemplateView.as_view(template_name="carparks/search.html"), name="search-carpark"),
    path("average-height/", TemplateView.as_view(template_name="carparks/average_gantry_height.html"), name="average-gantry-height"),
    path("group-by-system/", TemplateView.as_view(template_name="carparks/group_by_parking_system.html"), name="group-by-parking-system"),
    path("filter-by-type/", TemplateView.as_view(template_name="carparks/filter_by_type.html"), name="filter-by-type"),
    path("filter-free-parking/", TemplateView.as_view(template_name="carparks/filter_free_parking.html"), name="filter-free-parking"),
]
