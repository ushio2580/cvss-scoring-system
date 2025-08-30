#!/usr/bin/env python3

import jwt
import requests
import json
from datetime import datetime, timedelta

def test_jwt_creation():
    """Test JWT token creation and verification"""
    secret = 'dev-secret-key-change-in-production'
    
    # Create a token
    payload = {
        'sub': 1,  # user_id
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=24),
        'type': 'access'
    }
    
    print("1. Creating JWT token...")
    token = jwt.encode(payload, secret, algorithm='HS256')
    print(f"Token created: {token[:50]}...")
    
    # Verify the token
    print("\n2. Verifying JWT token...")
    try:
        decoded = jwt.decode(token, secret, algorithms=['HS256'])
        print(f"Token verified successfully: {decoded}")
        return token
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None

def test_backend_jwt():
    """Test backend JWT endpoints"""
    base_url = "http://localhost:5000/api"
    
    print("\n3. Testing backend login...")
    login_data = {
        "email": "admin@cvss.com",
        "password": "admin123"
    }
    
    response = requests.post(f"{base_url}/auth/login", json=login_data)
    print(f"Login status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        token = data['access_token']
        print(f"Backend token: {token[:50]}...")
        
        # Test token verification
        print("\n4. Testing token verification...")
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # Test with our own verification
        try:
            decoded = jwt.decode(token, 'dev-secret-key-change-in-production', algorithms=['HS256'])
            print(f"Our verification successful: {decoded}")
        except Exception as e:
            print(f"Our verification failed: {e}")
        
        # Test backend endpoints
        print("\n5. Testing backend endpoints...")
        
        # Test profile endpoint
        response = requests.get(f"{base_url}/auth/profile", headers=headers)
        print(f"Profile endpoint: {response.status_code} - {response.text[:100]}")
        
        # Test dashboard endpoint
        response = requests.get(f"{base_url}/dashboard/summary?days=30", headers=headers)
        print(f"Dashboard endpoint: {response.status_code} - {response.text[:100]}")
        
        return token
    else:
        print(f"Login failed: {response.text}")
        return None

if __name__ == "__main__":
    print("=== JWT Debug Test ===\n")
    
    # Test our own JWT
    our_token = test_jwt_creation()
    
    # Test backend JWT
    backend_token = test_backend_jwt()
    
    print("\n=== Summary ===")
    if our_token and backend_token:
        print("✅ Our JWT creation/verification works")
        print("✅ Backend JWT creation works")
        print("❌ Backend JWT verification fails")
        print("\nThe issue is likely in the Flask-JWT-Extended configuration")
    else:
        print("❌ JWT creation/verification has issues")
