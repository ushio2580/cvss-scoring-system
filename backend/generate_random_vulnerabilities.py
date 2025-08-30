#!/usr/bin/env python3
"""
Generate random vulnerabilities in JSON format for bulk upload testing
"""

import json
import random
from datetime import datetime

# Vulnerability templates
VULNERABILITY_TYPES = [
    {
        "name": "SQL Injection",
        "patterns": [
            "SQL Injection in {component}",
            "Blind SQL Injection in {component}",
            "Time-based SQL Injection in {component}",
            "Union-based SQL Injection in {component}"
        ],
        "descriptions": [
            "SQL injection vulnerability in {component} allowing unauthorized database access",
            "Blind SQL injection in {component} that can be exploited to extract sensitive data",
            "Time-based SQL injection in {component} that can be used for data exfiltration",
            "Union-based SQL injection in {component} allowing data retrieval"
        ],
        "vectors": [
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H",
            "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H"
        ],
        "severities": ["Critical", "High"]
    },
    {
        "name": "Cross-Site Scripting",
        "patterns": [
            "Cross-Site Scripting (XSS) in {component}",
            "Reflected XSS in {component}",
            "Stored XSS in {component}",
            "DOM-based XSS in {component}"
        ],
        "descriptions": [
            "Cross-site scripting vulnerability in {component} allowing script injection",
            "Reflected XSS in {component} that can be exploited via user input",
            "Stored XSS in {component} that persists in the application",
            "DOM-based XSS in {component} affecting client-side code"
        ],
        "vectors": [
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N",
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N",
            "CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N"
        ],
        "severities": ["High", "Medium"]
    },
    {
        "name": "Authentication",
        "patterns": [
            "Weak Password Policy in {component}",
            "Authentication Bypass in {component}",
            "Session Fixation in {component}",
            "Brute Force Vulnerability in {component}"
        ],
        "descriptions": [
            "Weak password requirements in {component} making accounts vulnerable",
            "Authentication bypass vulnerability in {component} allowing unauthorized access",
            "Session fixation vulnerability in {component} affecting user sessions",
            "Brute force vulnerability in {component} allowing account enumeration"
        ],
        "vectors": [
            "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L",
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N"
        ],
        "severities": ["Medium", "High"]
    },
    {
        "name": "Information Disclosure",
        "patterns": [
            "Information Disclosure in {component}",
            "Sensitive Data Exposure in {component}",
            "Directory Listing in {component}",
            "Error Information Disclosure in {component}"
        ],
        "descriptions": [
            "Information disclosure vulnerability in {component} exposing sensitive data",
            "Sensitive data exposure in {component} through improper handling",
            "Directory listing vulnerability in {component} exposing file structure",
            "Error information disclosure in {component} revealing system details"
        ],
        "vectors": [
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N",
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
            "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N"
        ],
        "severities": ["Medium", "Low"]
    },
    {
        "name": "Command Injection",
        "patterns": [
            "Command Injection in {component}",
            "OS Command Injection in {component}",
            "Remote Code Execution in {component}",
            "Code Injection in {component}"
        ],
        "descriptions": [
            "Command injection vulnerability in {component} allowing OS command execution",
            "OS command injection in {component} that can be exploited for system access",
            "Remote code execution vulnerability in {component} allowing arbitrary code execution",
            "Code injection vulnerability in {component} affecting application logic"
        ],
        "vectors": [
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
            "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H",
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H"
        ],
        "severities": ["Critical", "High"]
    }
]

COMPONENTS = [
    "Login Form", "Search Function", "File Upload", "User Profile", "Admin Panel",
    "API Endpoint", "Database Query", "Web Service", "Authentication System",
    "Session Management", "Password Reset", "User Registration", "Payment Gateway",
    "File Management", "Report Generation", "Data Export", "Configuration Panel"
]

SOURCES = ["internal", "nvd", "external"]
STATUSES = ["Open", "Mitigating", "Fixed", "Accepted"]

def generate_random_cve_id():
    """Generate a random CVE ID"""
    year = random.randint(2020, 2024)
    number = random.randint(1000, 9999)
    return f"CVE-{year}-{number:04d}"

def generate_random_vulnerability():
    """Generate a random vulnerability"""
    vuln_type = random.choice(VULNERABILITY_TYPES)
    component = random.choice(COMPONENTS)
    
    # Generate title
    pattern = random.choice(vuln_type["patterns"])
    title = pattern.format(component=component)
    
    # Generate description
    desc_pattern = random.choice(vuln_type["descriptions"])
    description = desc_pattern.format(component=component)
    
    # Generate CVE ID
    cve_id = generate_random_cve_id()
    
    # Select vector and severity
    vector = random.choice(vuln_type["vectors"])
    severity = random.choice(vuln_type["severities"])
    
    # Random status and source
    status = random.choice(STATUSES)
    source = random.choice(SOURCES)
    
    return {
        "title": title,
        "cve_id": cve_id,
        "description": description,
        "vector": vector,
        "severity": severity,
        "status": status,
        "source": source
    }

def generate_vulnerabilities_json(count=20, filename=None):
    """Generate a JSON file with random vulnerabilities"""
    vulnerabilities = []
    
    for i in range(count):
        vuln = generate_random_vulnerability()
        vulnerabilities.append(vuln)
    
    # Create the JSON structure
    json_data = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "total_vulnerabilities": count,
            "description": "Random vulnerabilities generated for testing bulk upload"
        },
        "vulnerabilities": vulnerabilities
    }
    
    # Save to file
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"random_vulnerabilities_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated {count} random vulnerabilities in '{filename}'")
    return filename

def generate_simple_json_array(count=20, filename=None):
    """Generate a simple JSON array format (for bulk upload)"""
    vulnerabilities = []
    
    for i in range(count):
        vuln = generate_random_vulnerability()
        vulnerabilities.append(vuln)
    
    # Save to file
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bulk_upload_vulnerabilities_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(vulnerabilities, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated {count} vulnerabilities in bulk upload format: '{filename}'")
    return filename

def main():
    """Main function"""
    print("🚀 Random Vulnerability Generator")
    print("=" * 50)
    
    # Generate different formats
    print("\n📝 Generating files...")
    
    # Simple array format (for bulk upload)
    simple_file = generate_simple_json_array(15, "bulk_upload_sample.json")
    
    # Detailed format with metadata
    detailed_file = generate_vulnerabilities_json(10, "detailed_vulnerabilities.json")
    
    print(f"\n📊 Files generated:")
    print(f"  📄 {simple_file} - Simple array format for bulk upload")
    print(f"  📄 {detailed_file} - Detailed format with metadata")
    
    print(f"\n💡 Usage:")
    print(f"  - Use '{simple_file}' for bulk upload testing")
    print(f"  - Use '{detailed_file}' for detailed analysis")

if __name__ == "__main__":
    main()
