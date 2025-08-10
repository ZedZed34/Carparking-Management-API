from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Health check endpoint
def health(_):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # Health check endpoint (used for Railway uptime & CI tests)
    path('healthz/', health),

    # API endpoints (assuming you have an app called 'carparks')
    path('api/carparks/', include('carparks.urls')),

    # If you have user auth endpoints (optional)
    # path('api/auth/', include('rest_framework.urls')),
]
