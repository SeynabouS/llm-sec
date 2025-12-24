#!/usr/bin/env python3
"""
Generate tests_flat.yaml from code snippets in snippets/ folder.
30 tests total: 10 Python + 10 JavaScript + 10 Java
"""

import os
import yaml
from pathlib import Path

# CWE mappings based on filename patterns
CWE_MAP = {
    "sql": "CWE-89",  # SQL Injection
    "cmd": "CWE-78",  # OS Command Injection
    "exec": "CWE-95", # Code Injection
    "deser": "CWE-502", # Deserialization
    "hash": "CWE-327", # Weak Hashing
    "eval": "CWE-95",  # Code Injection
    "xss": "CWE-79",   # XSS
    "xxe": "CWE-611",  # XXE
    "path_trav": "CWE-22", # Path Traversal
    "path": "CWE-22",  # Path Traversal
    "crypto": "CWE-327", # Weak Crypto
}

def get_cwe_from_filename(filename):
    """Extract CWE from filename."""
    lower_name = filename.lower()
    for pattern, cwe in CWE_MAP.items():
        if pattern in lower_name:
            return cwe
    return "CWE-Unknown"

def is_vulnerable(filename):
    """Determine if snippet is vulnerable based on filename.
    
    Pattern: odd-numbered files (01_, 03_, 05_, 07_, 09_) are vulnerable.
    Even-numbered files (02_, 04_, 06_, 08_, 10_) are safe.
    """
    # Extract the number from filename
    basename = os.path.basename(filename)
    parts = basename.split('_')
    if parts[0].isdigit():
        num = int(parts[0])
        return num % 2 == 1  # Odd = vulnerable
    return False

def read_snippet(filepath):
    """Read snippet content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read().strip()

def generate_tests():
    """Generate test list from snippets."""
    tests = []
    languages = ['python', 'javascript', 'java']
    
    for lang in languages:
        snippets_dir = f'snippets/{lang}'
        if not os.path.exists(snippets_dir):
            print(f"Warning: {snippets_dir} not found")
            continue
        
        # Get all snippet files
        files = sorted([f for f in os.listdir(snippets_dir) if f.startswith(('0', '1'))])
        
        for filename in files:
            filepath = os.path.join(snippets_dir, filename)
            if not os.path.isfile(filepath):
                continue
            
            code = read_snippet(filepath)
            is_vuln = is_vulnerable(filename)
            cwe = get_cwe_from_filename(filename)
            
            test = {
                'vars': {
                    'code': code,
                    'label': 'yes' if is_vuln else 'no',
                    'language': lang,
                    'cwe_hint': cwe,
                    'filename': filename
                }
            }
            tests.append(test)
            print(f"✅ {lang:10} | {filename:20} | Label: {'VULN' if is_vuln else 'SAFE':<4} | {cwe}")
    
    return tests

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 70)
    print("Generating tests_flat.yaml from snippets...")
    print("=" * 70)
    
    tests = generate_tests()
    
    # Create _generated directory
    os.makedirs('_generated', exist_ok=True)
    
    # Write YAML
    output_file = '_generated/tests_flat.yaml'
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(tests, f, default_flow_style=False, allow_unicode=True)
    
    print("\n" + "=" * 70)
    print(f"✅ Generated {len(tests)} tests → {output_file}")
    print("=" * 70)

if __name__ == '__main__':
    main()
