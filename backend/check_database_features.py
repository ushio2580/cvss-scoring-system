#!/usr/bin/env python3
"""
Script to check when database features are available
"""

import requests
import json
import time

BASE_URL = "https://cvss-scoring-system.onrender.com"

def login_as_admin():
    """Login as admin and get token"""
    login_data = {
        "email": "admin@cvss.com",
        "password": "admin123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data, timeout=10)
        if response.status_code == 200:
            return response.json().get('access_token')
        else:
            print(f"❌ Login failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Login error: {e}")
        return None

def check_endpoint(endpoint, token=None, method='GET', data=None):
    """Check if an endpoint is available"""
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    try:
        if method == 'GET':
            response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, timeout=10)
        elif method == 'POST':
            response = requests.post(f"{BASE_URL}{endpoint}", headers=headers, json=data, timeout=10)
        
        if response.status_code == 200:
            return True, response.json()
        elif response.status_code == 403:
            return False, "Access denied (not admin)"
        elif response.status_code == 404:
            return False, "Endpoint not found"
        else:
            return False, f"Status {response.status_code}"
            
    except Exception as e:
        return False, str(e)

def main():
    """Check all database features"""
    print("🔍 Checking database features availability...")
    print("=" * 50)
    
    # Check basic endpoints
    endpoints_to_check = [
        ("/", "GET", "Basic API"),
        ("/api/admin/database-status", "GET", "Database Status"),
        ("/api/database/info", "GET", "Database Info"),
        ("/api/database/backup/status", "GET", "Backup Status"),
    ]
    
    # First check without authentication
    print("\n📋 Checking endpoints without authentication:")
    for endpoint, method, description in endpoints_to_check:
        available, result = check_endpoint(endpoint, method=method)
        status = "✅ Available" if available else "❌ Not available"
        print(f"   {description}: {status}")
        if not available and "Access denied" not in str(result):
            print(f"      Error: {result}")
    
    # Login as admin
    print("\n🔐 Logging in as admin...")
    token = login_as_admin()
    
    if token:
        print("✅ Login successful")
        
        print("\n📋 Checking endpoints with admin authentication:")
        for endpoint, method, description in endpoints_to_check:
            available, result = check_endpoint(endpoint, token=token, method=method)
            status = "✅ Available" if available else "❌ Not available"
            print(f"   {description}: {status}")
            if available and isinstance(result, dict):
                print(f"      Response: {json.dumps(result, indent=6)}")
            elif not available:
                print(f"      Error: {result}")
    else:
        print("❌ Could not login as admin")
    
    print("\n" + "=" * 50)
    print("💡 When all endpoints are available, you can:")
    print("   1. Access Database Manager in the frontend")
    print("   2. Create database backups")
    print("   3. Export data in various formats")
    print("   4. Execute SQL queries")
    print("   5. Monitor database status")

if __name__ == "__main__":
    main()
