#!/usr/bin/env python3
"""
CVSS Vector Examples
Ejemplos de vectores CVSS válidos para el sistema
"""

EXAMPLES = [
    {
        "name": "Critical SQL Injection",
        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
        "score": "9.8",
        "severity": "Critical"
    },
    {
        "name": "High Cross-Site Scripting (XSS)",
        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N",
        "score": "6.1",
        "severity": "Medium"
    },
    {
        "name": "Medium Weak Password Policy",
        "vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L",
        "score": "5.3",
        "severity": "Medium"
    },
    {
        "name": "Low Information Disclosure",
        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N",
        "score": "5.3",
        "severity": "Medium"
    },
    {
        "name": "Critical Remote Code Execution",
        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
        "score": "9.8",
        "severity": "Critical"
    }
]

def print_examples():
    print("🔍 CVSS Vector Examples - Ejemplos de Vectores CVSS")
    print("=" * 60)
    print()
    
    for i, example in enumerate(EXAMPLES, 1):
        print(f"{i}. {example['name']}")
        print(f"   Vector: {example['vector']}")
        print(f"   Score: {example['score']} ({example['severity']})")
        print()
    
    print("📝 Formatos Aceptados:")
    print("   ✅ CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H")
    print("   ✅ CVSS:AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H")
    print("   ✅ AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H")
    print()
    print("❌ Formatos NO válidos:")
    print("   ❌ CVSS: AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H")
    print("   ❌ AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H (sin CVSS:)")
    print()

if __name__ == "__main__":
    print_examples()
