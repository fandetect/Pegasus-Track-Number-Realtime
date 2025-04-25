#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup environment for Pegasus Track Number Realtime
"""

import os
import sys
import subprocess
import platform
import importlib.util

def check_packages():
    """Check if required packages are installed"""
    print("Checking required packages...")
    required_packages = ["phonenumbers", "opencage", "termcolor"]
    missing_packages = []
    
    for package in required_packages:
        if importlib.util.find_spec(package) is None:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        return False
    else:
        print("✅ All required packages are installed.")
        return True

def install_packages():
    """Install required packages"""
    print("Installing required packages...")
    python_cmd = "python" if platform.system() == "Windows" else "python3"
    try:
        subprocess.check_call([python_cmd, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully.")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Try running manually:")
        print("   pip install -r requirements.txt")
        return False

def setup_api_key():
    """Help the user set up the OpenCage API key"""
    print("\nOpenCage API Key Setup:")
    print("An OpenCage API key is required for full location functionality.")
    print("You can get a free API key from https://opencagedata.com/")
    
    current_key = os.environ.get("OPENCAGE_API_KEY")
    if current_key and current_key != "YOUR_OPENCAGE_API_KEY":
        print(f"✅ OpenCage API key is already set in the environment.")
        return
    
    print("\nWould you like to set the API key now? (y/n): ", end="")
    response = input().lower()
    
    if response == 'y':
        print("Enter your OpenCage API key: ", end="")
        api_key = input().strip()
        
        if platform.system() == "Windows":
            print(f"\nTo set the API key on Windows, run this command:")
            print(f'setx OPENCAGE_API_KEY "{api_key}"')
            print("(You'll need to restart your terminal after running this command)")
        else:
            print(f"\nTo set the API key on Linux/macOS, add this line to your ~/.bashrc or ~/.zshrc:")
            print(f'export OPENCAGE_API_KEY="{api_key}"')
        
        print("\nAlternatively, you can set it just for this session:")
        if platform.system() == "Windows":
            print(f'set OPENCAGE_API_KEY={api_key}')
        else:
            print(f'export OPENCAGE_API_KEY={api_key}')

def main():
    """Main setup function"""
    print("🛰️ Pegasus Track Number Realtime - Setup\n")
    
    if not check_packages():
        print("\nInstalling missing packages...")
        if not install_packages():
            sys.exit(1)
        
        # Check again after installation
        if not check_packages():
            print("❌ Some packages are still missing after installation.")
            print("Please try to install them manually:")
            print("pip install -r requirements.txt")
            sys.exit(1)
    
    setup_api_key()
    
    print("\n✅ Setup completed successfully!")
    print("You can now run the main script:")
    print("python pegasus-track-number-realtime.py")

if __name__ == "__main__":
    main() 