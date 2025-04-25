#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🛰️ Pegasus Track Number Realtime
Author: Letda Kes dr. Sobri, S.Kom
Email: muhammadsobrimaulana31@gmail.com
GitHub: https://github.com/sobri3195
Support: https://lynk.id/muhsobrimaulana
"""

import os
import sys
import hashlib
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from opencage.geocoder import OpenCageGeocode
from termcolor import colored

# Anti-modification protection
ORIGINAL_CHECKSUM = "b6ab9e654f9c56392e5a6dbd90be9648"  # Real checksum of this file

class PegasusTracker:
    def __init__(self):
        self.activation_key = "sobri"
        # You can get a free API key from https://opencagedata.com/
        self.api_key = os.environ.get("OPENCAGE_API_KEY", "YOUR_OPENCAGE_API_KEY") 
        self.geocoder = None  # Will be initialized when needed
        self.default_country = "Indonesia"
    
    def verify_integrity(self):
        with open(__file__, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the checksum line from the hash calculation
        content_for_hash = "\n".join([line for line in content.split('\n') 
                                    if "ORIGINAL_CHECKSUM =" not in line])
        
        current_hash = hashlib.md5(content_for_hash.encode()).hexdigest()
        
        if current_hash != ORIGINAL_CHECKSUM and ORIGINAL_CHECKSUM != "e37d1824d0c76f9d0e5ca24c4e9a9aa0":
            print(colored("⚠️ ERROR: File has been modified! Exiting for security reasons.", "red"))
            sys.exit(1)
    
    def verify_activation(self):
        attempt = input("Masukkan kata aktivasi: ")
        if attempt != self.activation_key:
            print(colored("⚠️ Aktivasi gagal! Kode tidak valid.", "red"))
            sys.exit(1)
        print(colored("✅ Aktivasi berhasil!", "green"))
    
    def validate_phone_number(self, number):
        try:
            parsed = phonenumbers.parse(number)
            if not phonenumbers.is_valid_number(parsed):
                raise ValueError("Nomor tidak valid")
            return parsed
        except Exception as e:
            print(colored(f"⚠️ ERROR: {str(e)}", "red"))
            sys.exit(1)
    
    def get_country_flag(self, country_code):
        # Convert country code to flag emoji
        if len(country_code) != 2:
            return "🏳️"
        
        # Unicode flag emoji offset
        OFFSET = ord('🇦') - ord('A')
        
        # Convert country code to uppercase
        code = country_code.upper()
        
        # Convert each letter to regional indicator symbol
        return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)
    
    def track_number(self, number):
        parsed_number = self.validate_phone_number(number)
        
        # Get basic info
        country_code = phonenumbers.region_code_for_number(parsed_number)
        country_name = geocoder.description_for_number(parsed_number, "en") or self.default_country
        carrier_name = carrier.name_for_number(parsed_number, "en") or "Unknown"
        timezones = timezone.time_zones_for_number(parsed_number)
        
        # Get location data if possible
        try:
            # Initialize geocoder only when needed
            if self.geocoder is None:
                if self.api_key == "YOUR_OPENCAGE_API_KEY":
                    print(colored("\n⚠️ OpenCage API key tidak dikonfigurasi. Informasi lokasi akan terbatas.", "yellow"))
                    print(colored("Dapatkan API key gratis di https://opencagedata.com/\n", "yellow"))
                    raise ValueError("API key not configured")
                self.geocoder = OpenCageGeocode(self.api_key)
                
            results = self.geocoder.geocode(country_name)
            if results and len(results):
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']
                currency = results[0]['annotations'].get('currency', {}).get('name', 'Unknown')
                timezone_info = results[0]['annotations'].get('timezone', {}).get('name', 'Unknown')
                flag = self.get_country_flag(country_code)
                map_url = f"https://www.openstreetmap.org/?lat={lat}&lon={lng}"
            else:
                lat, lng = "Unknown", "Unknown"
                currency, timezone_info = "Unknown", "Unknown"
                flag = "🏳️"
                map_url = "https://www.openstreetmap.org/"
        except Exception:
            lat, lng = "Unknown", "Unknown" 
            currency, timezone_info = "Unknown", "Unknown"
            flag = "🏳️"
            map_url = "https://www.openstreetmap.org/"
        
        # Display results
        print("\n" + "="*50)
        print(colored(f"Country Name => {country_name}", "cyan"))
        print("-"*25)
        print(colored(f"Telecom Company Name => {carrier_name}", "cyan"))
        print("-"*25)
        
        if lat != "Unknown" and lng != "Unknown":
            print(f"Latitude: {lat}")
            print(f"Longitude: {lng}")
        
        print(f"Currency: {currency}")
        print(f"Timezone: {timezone_info}")
        print(f"Flag: {flag}")
        print(f"Map: {map_url}")
        print("="*50 + "\n")

def print_header():
    header = """
🛰️ Pegasus Track Number Realtime 🛰️
-----------------------------------
Author: Letda Kes dr. Sobri, S.Kom
Email: muhammadsobrimaulana31@gmail.com
GitHub: https://github.com/sobri3195
Support: https://lynk.id/muhsobrimaulana
-----------------------------------
"""
    print(colored(header, "yellow"))

def main():
    print_header()
    
    tracker = PegasusTracker()
    tracker.verify_integrity()
    tracker.verify_activation()
    
    number = input("Masukkan nomor telepon: ")
    tracker.track_number(number)
    
    print(colored("\n⚠️ Peringatan: Gunakan hanya untuk tujuan edukasi & keamanan pribadi", "red"))
    print(colored("© 2025 Letda Kes dr. Sobri, S.Kom - Lisensi Khusus", "magenta"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(colored(f"⚠️ ERROR: {str(e)}", "red")) 