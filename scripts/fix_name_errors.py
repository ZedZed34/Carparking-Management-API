#!/usr/bin/env python
"""
Script to fix the #NAME? address errors in the carpark database
"""

import os
import sys
import django

# Add project to path and setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvancedWebDevelopment.settings")
django.setup()

from carparks.models import CarPark

def fix_name_errors():
    """Fix or remove records with #NAME? addresses"""
    
    # Find all records with #NAME? in address
    bad_records = CarPark.objects.filter(address='#NAME?')
    
    print(f"Found {bad_records.count()} records with #NAME? addresses:")
    
    for record in bad_records:
        print(f"  - ID: {record.id}, Car Park No: {record.car_park_no}, Type: {record.car_park_type}")
        print(f"    Coordinates: ({record.x_coord}, {record.y_coord})")
    
    # Option 1: Try to map car park numbers to known locations
    known_mappings = {
        'HE19': 'HENDERSON ROAD',
        'Q49': 'QUEENSTOWN AREA',
        'TE26': 'TELOK BLANGAH AREA', 
        'W16': 'WOODLANDS AREA'
    }
    
    print("\nFixing records...")
    fixed_count = 0
    
    for record in bad_records:
        if record.car_park_no in known_mappings:
            new_address = known_mappings[record.car_park_no]
            print(f"  Updating {record.car_park_no}: #NAME? → {new_address}")
            record.address = new_address
            record.save()
            fixed_count += 1
        else:
            print(f"  No mapping found for {record.car_park_no}")
    
    print(f"\nFixed {fixed_count} records.")
    
    # Option 2: Remove unfixable records (optional)
    remaining_bad = CarPark.objects.filter(address='#NAME?')
    if remaining_bad.exists():
        print(f"\nStill have {remaining_bad.count()} records with #NAME? addresses.")
        response = input("Do you want to delete these records? (y/N): ")
        
        if response.lower() == 'y':
            deleted_count = remaining_bad.count()
            remaining_bad.delete()
            print(f"Deleted {deleted_count} records with #NAME? addresses.")
        else:
            print("Keeping records with #NAME? addresses.")
    
    print("\nData cleanup complete!")

def show_summary():
    """Show summary of carpark data"""
    total = CarPark.objects.count()
    bad_records = CarPark.objects.filter(address='#NAME?').count()
    good_records = total - bad_records
    
    print(f"\nDatabase Summary:")
    print(f"  Total carparks: {total}")
    print(f"  Valid addresses: {good_records}")
    print(f"  #NAME? addresses: {bad_records}")
    
    if bad_records == 0:
        print("  ✅ All addresses are valid!")
    else:
        print(f"  ⚠️  {bad_records} addresses need fixing")

if __name__ == "__main__":
    print("🔧 Carpark Address Cleanup Tool")
    print("=" * 40)
    
    show_summary()
    
    bad_records = CarPark.objects.filter(address='#NAME?')
    if bad_records.exists():
        print("\n🚨 Found records with #NAME? addresses")
        response = input("\nDo you want to fix these records? (Y/n): ")
        
        if response.lower() != 'n':
            fix_name_errors()
            show_summary()
        else:
            print("Skipping fixes.")
    else:
        print("\n✅ No #NAME? addresses found. Database is clean!")
