#!/usr/bin/env python
"""
Simple script to test if the Django installation is working properly
"""

import os
import sys
import django

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configure Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvancedWebDevelopment.settings")

def test_django_setup():
    """Test if Django can be set up properly"""
    try:
        django.setup()
        print("✅ Django setup successful")
        return True
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        return False

def test_database_connection():
    """Test if database connection works"""
    try:
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("✅ Database connection successful")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def test_models():
    """Test if models can be imported"""
    try:
        from carparks.models import CarPark
        count = CarPark.objects.count()
        print(f"✅ Models working - Found {count} carparks")
        return True
    except Exception as e:
        print(f"❌ Models test failed: {e}")
        return False

def test_api_views():
    """Test if API views can be imported"""
    try:
        from carparks.views import CarParkListView
        print("✅ API views import successful")
        return True
    except Exception as e:
        print(f"❌ API views import failed: {e}")
        return False

def test_optional_dependencies():
    """Test optional dependencies"""
    dependencies = {
        'whitenoise': 'Static file serving',
        'dj_database_url': 'Database URL parsing',
        'psycopg2': 'PostgreSQL adapter',
        'gunicorn': 'Production server',
        'python_dotenv': 'Environment variables'
    }
    
    print("\n📦 Optional Dependencies Check:")
    for dep, description in dependencies.items():
        try:
            __import__(dep)
            print(f"✅ {dep}: {description}")
        except ImportError:
            print(f"⚠️  {dep}: {description} (not installed)")

if __name__ == "__main__":
    print("🧪 Testing Django Carpark API Installation\n")
    
    tests = [
        ("Django Setup", test_django_setup),
        ("Database Connection", test_database_connection),
        ("Models", test_models),
        ("API Views", test_api_views),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        if test_func():
            passed += 1
    
    test_optional_dependencies()
    
    print(f"\n📊 Test Results: {passed}/{total} core tests passed")
    
    if passed == total:
        print("🎉 All core tests passed! The installation is working correctly.")
        print("\n🚀 Next steps:")
        print("1. Run: python manage.py runserver")
        print("2. Visit: http://localhost:8000/api/v1/carparks/")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you're in the virtual environment")
        print("2. Run: pip install -r requirements.txt")
        print("3. Run: python manage.py migrate")
        sys.exit(1)
