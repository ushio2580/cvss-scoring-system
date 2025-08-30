#!/usr/bin/env python3
"""
Debug script for bulk upload with detailed error reporting
"""

import requests
import json
import os

# Configuration
BASE_URL = "http://localhost:5000/api"
LOGIN_DATA = {
    "email": "admin@cvss.com",
    "password": "admin123"
}

def test_login():
    """Test login and get token"""
    print("🔐 Testing login...")
    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=LOGIN_DATA, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            token = data.get('access_token')
            print(f"✅ Login successful! Token: {token[:50]}...")
            return token
        else:
            print(f"❌ Login failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except requests.exceptions.ConnectionError:
        print("❌ Connection refused. Is the backend running?")
        return None
    except Exception as e:
        print(f"❌ Login error: {e}")
        return None

def test_bulk_upload_with_details(token):
    """Test bulk upload with detailed error reporting"""
    print("\n📤 Testing bulk upload with detailed error reporting...")
    
    # Check if sample file exists
    if not os.path.exists("sample_vulnerabilities_unique.csv"):
        print("❌ Sample file not found!")
        return False
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        with open("sample_vulnerabilities_unique.csv", "rb") as f:
            files = {"file": ("sample_vulnerabilities_unique.csv", f, "text/csv")}
            response = requests.post(f"{BASE_URL}/bulk/upload", headers=headers, files=files, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Bulk upload successful!")
            print(f"📊 Results: {json.dumps(data, indent=2)}")
            
            # Show detailed error analysis
            if data.get('results', {}).get('errors'):
                print("\n🔍 Error Analysis:")
                for i, error in enumerate(data['results']['errors'], 1):
                    print(f"  {i}. {error}")
            
            return True
        else:
            print(f"❌ Bulk upload failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection refused. Is the backend running?")
        return False
    except Exception as e:
        print(f"❌ Upload error: {e}")
        return False

def test_single_vulnerability_creation(token):
    """Test creating a single vulnerability to verify the system works"""
    print("\n🧪 Testing single vulnerability creation...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    test_data = {
        "title": "Test Vulnerability for Debug",
        "cve_id": "CVE-2024-DEBUG-001",
        "description": "Test vulnerability for debugging bulk upload",
        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L",
        "severity": "Medium",
        "status": "Open",
        "source": "internal"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/vulns/", headers=headers, json=test_data, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 201:
            data = response.json()
            print("✅ Single vulnerability creation successful!")
            print(f"Created vulnerability: {data.get('vulnerability', {}).get('title')}")
            return True
        else:
            print(f"❌ Single vulnerability creation failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Single vulnerability creation error: {e}")
        return False

def main():
    """Run debug tests"""
    print("🚀 Starting bulk upload debug tests...")
    print("=" * 60)
    
    # Test login
    token = test_login()
    if not token:
        print("❌ Cannot continue without valid token")
        return
    
    # Test single vulnerability creation first
    test_single_vulnerability_creation(token)
    
    # Test bulk upload with detailed reporting
    test_bulk_upload_with_details(token)
    
    print("\n" + "=" * 60)
    print("🏁 Debug tests completed!")

if __name__ == "__main__":
    main()
