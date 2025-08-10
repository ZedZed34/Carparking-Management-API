#!/usr/bin/env python
"""
Script to create a Django superuser using environment variables
This is useful for Railway deployment where interactive prompts aren't available
"""

import os
import sys
import django

# Add project to path and setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvancedWebDevelopment.settings")
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    """Create a superuser using environment variables"""
    
    User = get_user_model()
    
    # Get credentials from environment variables
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")
    
    # Check if superuser already exists
    if User.objects.filter(username=username).exists():
        print(f"Superuser '{username}' already exists.")
        return
    
    # Create superuser
    try:
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"✅ Superuser '{username}' created successfully!")
        print(f"   Email: {email}")
        print(f"   Password: {'*' * len(password)}")
    except Exception as e:
        print(f"❌ Error creating superuser: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("🔧 Creating Django Superuser")
    print("=" * 30)
    create_superuser()
