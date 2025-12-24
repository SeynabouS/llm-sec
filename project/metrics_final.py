#!/usr/bin/env python3
"""
Calculate Final Project metrics from evaluation results.
Metrics:
- json_rate: % of outputs that are valid JSON
- citation_rate: % of RAG outputs with citations
- safety_field_rate: % of outputs with 'safety' field
"""

import json
import csv
import sys
import os

def calculate_metrics(results_json):
    """Calculate metrics from evaluation results."""
    
    try:
        with open(results_json, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading {results_json}: {e}")
        return None
    
    # Get results array
    if isinstance(data, dict):
        results = data.get('results', [])
    else:
        results = data
    
    if not results:
        print(f"❌ No results found")
        return None
    
    total = len(results)
    json_count = 0
    citation_count = 0
    safety_count = 0
    
    for r in results:
        # Get response object
        resp = r.get('response')
        if resp is None:
            resp = r.get('output')
            if isinstance(resp, str):
                try:
                    resp = json.loads(resp)
                except:
                    continue
        
        if isinstance(resp, dict):
            json_count += 1
            
            # Check for citations
            if resp.get('citations') and len(resp.get('citations', [])) > 0:
                citation_count += 1
            
            # Check for safety field
            if 'safety' in resp:
                safety_count += 1
    
    metrics = {
        'json_rate': json_count / total if total > 0 else 0,
        'citation_rate': citation_count / total if total > 0 else 0,
        'safety_field_rate': safety_count / total if total > 0 else 0,
        'total_tests': total,
        'json_count': json_count,
        'citation_count': citation_count,
        'safety_count': safety_count
    }
    
    return metrics

def write_csv(metrics, output_csv):
    """Write metrics to CSV."""
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['metric', 'value'])
        writer.writerow(['json_rate', f"{metrics['json_rate']:.3f}"])
        writer.writerow(['citation_rate', f"{metrics['citation_rate']:.3f}"])
        writer.writerow(['safety_field_rate', f"{metrics['safety_field_rate']:.3f}"])

def main():
    if len(sys.argv) < 2:
        print("Usage: python metrics_final.py <results.json> [output.csv]")
        sys.exit(1)
    
    results_json = sys.argv[1]
    output_csv = sys.argv[2] if len(sys.argv) > 2 else "reports/metrics.csv"
    
    if not os.path.exists(results_json):
        print(f"❌ {results_json} not found!")
        sys.exit(1)
    
    metrics = calculate_metrics(results_json)
    if metrics is None:
        sys.exit(1)
    
    os.makedirs(os.path.dirname(output_csv) or '.', exist_ok=True)
    write_csv(metrics, output_csv)
    
    # Display
    print("=" * 70)
    print("FINAL PROJECT METRICS")
    print("=" * 70)
    print(f"\nTotal Tests: {metrics['total_tests']}")
    print(f"Valid JSON:  {metrics['json_count']}/{metrics['total_tests']} → {metrics['json_rate']:6.1%}")
    print(f"Citations:   {metrics['citation_count']}/{metrics['total_tests']} → {metrics['citation_rate']:6.1%}")
    print(f"Safety Field:{metrics['safety_count']}/{metrics['total_tests']} → {metrics['safety_field_rate']:6.1%}")
    
    print("\n" + "=" * 70)
    print("THRESHOLD CHECKS")
    print("=" * 70)
    
    thresholds = {
        'json_rate': (0.95, 'JSON Validity'),
        'citation_rate': (0.80, 'Citation Rate'),
        'safety_field_rate': (0.85, 'Safety Classification')
    }
    
    for key, (threshold, label) in thresholds.items():
        value = metrics[key]
        status = "✅ PASS" if value >= threshold else "⚠️ WARN"
        print(f"{label:20} {value:6.1%} (target: {threshold:5.0%}) {status}")
    
    print("\n" + "=" * 70)
    print(f"✅ Metrics written to: {output_csv}")
    print("=" * 70)

if __name__ == '__main__':
    main()
