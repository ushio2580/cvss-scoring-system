#!/usr/bin/env python3
"""
Remote database initialization script
Creates test users and data via API calls
"""

import requests
import json
import time

BASE_URL = "https://cvss-scoring-system.onrender.com"

def test_connection():
    """Test if the backend is accessible"""
    try:
        response = requests.get(f"{BASE_URL}/", timeout=10)
        if response.status_code == 200:
            print("✅ Backend is accessible")
            return True
        else:
            print(f"❌ Backend returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to backend: {e}")
        return False

def create_user(email, password, name, role):
    """Create a user via API"""
    try:
        data = {
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }
        
        response = requests.post(f"{BASE_URL}/api/auth/register", json=data, timeout=10)
        
        if response.status_code == 201:
            print(f"✅ Created user: {email}")
            return True
        elif response.status_code == 400 and "already exists" in response.text:
            print(f"ℹ️  User already exists: {email}")
            return True
        else:
            print(f"❌ Failed to create user {email}: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error creating user {email}: {e}")
        return False

def test_login(email, password):
    """Test login with given credentials"""
    try:
        data = {
            "email": email,
            "password": password
        }
        
        response = requests.post(f"{BASE_URL}/api/auth/login", json=data, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ Login successful: {email}")
            return True
        else:
            print(f"❌ Login failed for {email}: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing login for {email}: {e}")
        return False

def main():
    """Main function to initialize the database"""
    print("🚀 Initializing remote database...")
    
    # Test connection
    if not test_connection():
        print("❌ Cannot proceed - backend is not accessible")
        return
    
    # Create test users
    users = [
        {
            "email": "admin@cvss.com",
            "password": "admin123",
            "name": "Admin User",
            "role": "admin"
        },
        {
            "email": "analyst@cvss.com",
            "password": "analyst123",
            "name": "Analyst User",
            "role": "analyst"
        },
        {
            "email": "viewer@cvss.com",
            "password": "viewer123",
            "name": "Viewer User",
            "role": "viewer"
        }
    ]
    
    print("\n📝 Creating test users...")
    for user in users:
        create_user(user["email"], user["password"], user["name"], user["role"])
        time.sleep(1)  # Small delay between requests
    
    print("\n🔐 Testing login credentials...")
    for user in users:
        test_login(user["email"], user["password"])
        time.sleep(1)  # Small delay between requests
    
    print("\n🎉 Database initialization complete!")
    print("\n📋 Test users created:")
    for user in users:
        print(f"   {user['email']} / {user['password']} ({user['role']})")
    
    print("\n💡 You can now use these credentials to log in to your application!")

if __name__ == "__main__":
    main()
