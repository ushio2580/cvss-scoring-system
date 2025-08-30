#!/usr/bin/env python3
"""
Script to check audit logs and verify IP addresses
"""

import requests
import json

BASE_URL = "https://cvss-scoring-system.onrender.com"

def login_and_check_logs():
    """Login and check recent audit logs"""
    
    # Login data
    login_data = {
        "email": "admin@cvss.com",
        "password": "admin123"
    }
    
    print("🔐 Logging in...")
    
    try:
        # Login
        response = requests.post(
            f"{BASE_URL}/api/auth/login",
            json=login_data,
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ Login successful")
            token = response.json().get('access_token')
            
            if token:
                # Get audit logs
                headers = {
                    "Authorization": f"Bearer {token}"
                }
                
                print("\n📋 Getting recent audit logs...")
                audit_response = requests.get(
                    f"{BASE_URL}/api/audit/logs?per_page=10",
                    headers=headers,
                    timeout=10
                )
                
                if audit_response.status_code == 200:
                    data = audit_response.json()
                    logs = data.get('logs', [])
                    
                    if logs:
                        print(f"\n📊 Found {len(logs)} recent audit logs:")
                        print("=" * 80)
                        
                        for i, log in enumerate(logs, 1):
                            print(f"\n{i}. Action: {log.get('action')}")
                            print(f"   User: {log.get('username')} ({log.get('user_email', 'N/A')})")
                            print(f"   IP Address: {log.get('ip_address')}")
                            print(f"   User Agent: {log.get('user_agent', 'N/A')[:50]}...")
                            print(f"   Timestamp: {log.get('created_at')}")
                            print(f"   Target: {log.get('target_type')} - {log.get('target_name', 'N/A')}")
                            print("-" * 40)
                    else:
                        print("❌ No audit logs found")
                else:
                    print(f"❌ Failed to get audit logs: {audit_response.status_code}")
                    print(f"Response: {audit_response.text}")
            else:
                print("❌ No token received")
        else:
            print(f"❌ Login failed: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def test_different_ips():
    """Test with different IP headers"""
    
    users = [
        {"email": "admin@cvss.com", "password": "admin123"},
        {"email": "analyst@cvss.com", "password": "analyst123"},
        {"email": "viewer@cvss.com", "password": "viewer123"}
    ]
    
    print("\n🌐 Testing with different IP headers...")
    
    for i, user in enumerate(users, 1):
        print(f"\n--- Test {i}: {user['email']} ---")
        
        # Different IP scenarios
        headers = {
            "User-Agent": f"Test-Client/{i}.0",
            "X-Forwarded-For": f"192.168.1.{100 + i}, 10.0.0.1",
            "X-Real-IP": f"203.0.113.{i}",
            "CF-Connecting-IP": f"198.51.100.{i}"
        }
        
        try:
            response = requests.post(
                f"{BASE_URL}/api/auth/login",
                json=user,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✅ Login successful")
                token = response.json().get('access_token')
                
                if token:
                    # Get the most recent log
                    audit_headers = {"Authorization": f"Bearer {token}"}
                    audit_response = requests.get(
                        f"{BASE_URL}/api/audit/logs?per_page=1",
                        headers=audit_headers,
                        timeout=10
                    )
                    
                    if audit_response.status_code == 200:
                        logs = audit_response.json().get('logs', [])
                        if logs:
                            latest_log = logs[0]
                            print(f"📝 Latest log IP: {latest_log.get('ip_address')}")
                            print(f"   Headers sent: X-Forwarded-For={headers['X-Forwarded-For']}")
                            print(f"   Headers sent: X-Real-IP={headers['X-Real-IP']}")
                            print(f"   Headers sent: CF-Connecting-IP={headers['CF-Connecting-IP']}")
            else:
                print(f"❌ Login failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    login_and_check_logs()
    test_different_ips()

