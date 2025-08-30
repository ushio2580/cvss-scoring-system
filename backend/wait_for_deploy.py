#!/usr/bin/env python3
"""
Script to wait for deploy completion and check new features
"""

import requests
import time
import json

BASE_URL = "https://cvss-scoring-system.onrender.com"

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
            return None
    except Exception as e:
        return None

def main():
    """Wait for deploy and check features"""
    print("⏳ Esperando que el deploy se complete...")
    print("=" * 50)
    
    # Endpoints to check
    endpoints_to_check = [
        ("/api/admin/database-status", "GET", "Database Status"),
        ("/api/database/backup/status", "GET", "Backup Status"),
        ("/api/database/backup", "POST", "Backup Creation"),
        ("/api/database/export/full", "GET", "Full Export"),
    ]
    
    max_attempts = 30  # 30 attempts = 5 minutes
    attempt = 0
    
    while attempt < max_attempts:
        attempt += 1
        print(f"\n🔄 Intento {attempt}/{max_attempts} - Verificando endpoints...")
        
        # Login as admin
        token = login_as_admin()
        if not token:
            print("❌ No se pudo hacer login como admin")
            time.sleep(10)
            continue
        
        all_available = True
        
        for endpoint, method, description in endpoints_to_check:
            available, result = check_endpoint(endpoint, token=token, method=method)
            status = "✅ Disponible" if available else "❌ No disponible"
            print(f"   {description}: {status}")
            
            if not available:
                all_available = False
                if "Endpoint not found" in str(result):
                    print(f"      ⏳ Endpoint aún no desplegado")
                else:
                    print(f"      Error: {result}")
            else:
                print(f"      ✅ Funcionando correctamente")
        
        if all_available:
            print("\n🎉 ¡Deploy completado! Todas las funcionalidades están disponibles.")
            print("\n📋 Funcionalidades disponibles:")
            print("   • Backup completo de la base de datos")
            print("   • Exportación de datos en JSON")
            print("   • Estado de la base de datos")
            print("   • Gestión completa de la BD")
            print("\n🚀 ¡Tu aplicación está lista!")
            return
        
        print(f"\n⏳ Esperando 10 segundos antes del siguiente intento...")
        time.sleep(10)
    
    print(f"\n❌ Tiempo de espera agotado después de {max_attempts} intentos.")
    print("💡 El deploy puede estar tardando más de lo esperado.")
    print("   Puedes verificar manualmente más tarde.")

if __name__ == "__main__":
    main()
