"""AdvancedWebDevelopment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.generic import RedirectView

# Health check endpoint for Railway/Docker
def health_check(request):
    try:
        # Try to query the database to ensure it's working
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        db_status = "connected"
    except:
        db_status = "disconnected"
    
    return JsonResponse({
        "status": "healthy",
        "service": "Carpark Management API",
        "version": "1.0.0",
        "database": db_status
    })

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    
    # Health check endpoint
    path('health/', health_check, name='health'),
    path('healthz/', health_check, name='healthz'),  # Alternative for Railway
    
    # Root redirect
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    
    # Include carparks app URLs (includes both API and HTML views)
    path('', include('carparks.urls')),
    
    # Django REST Framework browsable API authentication
    path('api-auth/', include('rest_framework.urls')),
]
