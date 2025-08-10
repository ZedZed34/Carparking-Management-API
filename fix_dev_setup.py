#!/usr/bin/env python
"""
Quick fix script to get development server running on Windows
This script temporarily modifies settings to work without optional dependencies
"""

import os
import sys

def fix_settings():
    """Fix settings.py for development"""
    settings_path = "AdvancedWebDevelopment/settings.py"
    
    # Read current settings
    with open(settings_path, 'r') as f:
        content = f.read()
    
    # Check if already fixed
    if 'DEVELOPMENT_MODE = True' in content:
        print("✅ Settings already fixed for development")
        return
    
    # Add development mode flag at the top
    lines = content.split('\n')
    
    # Find the import section and add our flag
    for i, line in enumerate(lines):
        if line.startswith('import os'):
            lines.insert(i + 1, '\n# Development mode flag\nDEVELOPMENT_MODE = True')
            break
    
    # Write back the modified content
    with open(settings_path, 'w') as f:
        f.write('\n'.join(lines))
    
    print("✅ Settings.py updated for development mode")

def check_django():
    """Check if Django is working"""
    try:
        import django
        print(f"✅ Django {django.get_version()} is installed")
        return True
    except ImportError:
        print("❌ Django not found. Installing...")
        os.system("pip install Django==5.2.5")
        return False

def check_drf():
    """Check if Django REST Framework is working"""
    try:
        import rest_framework
        print(f"✅ Django REST Framework is installed")
        return True
    except ImportError:
        print("❌ Django REST Framework not found. Installing...")
        os.system("pip install djangorestframework==3.15.2")
        return False

def run_checks():
    """Run Django system checks"""
    print("\n🔍 Running Django system checks...")
    os.system("python manage.py check")

def main():
    print("🔧 Quick Development Setup Fix")
    print("=" * 40)
    
    # Check and install core dependencies
    check_django()
    check_drf()
    
    # Fix settings
    fix_settings()
    
    # Run checks
    run_checks()
    
    print("\n🎉 Development setup complete!")
    print("\nNext steps:")
    print("1. python manage.py migrate")
    print("2. python scripts/load_and_store.py")
    print("3. python manage.py runserver")

if __name__ == "__main__":
    main()
