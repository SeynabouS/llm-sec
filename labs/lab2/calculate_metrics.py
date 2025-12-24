#!/usr/bin/env python3
"""
Calculate metrics (precision, recall, F1) from Lab 2 evaluation results.
"""

import json
import csv
import os
from collections import defaultdict

def calculate_metrics(results_json):
    """Calculate TP, FP, TN, FN, precision, recall, F1 for each prompt."""
    
    with open(results_json, 'r') as f:
        data = json.load(f)
    
    results_by_prompt = defaultdict(lambda: {'TP': 0, 'FP': 0, 'TN': 0, 'FN': 0})
    
    # Process each evaluation result
    for result in data['results']:
        prompt_id = result['prompt']
        expected = result['expected']
        
        # Parse actual from JSON output
        try:
            output_obj = json.loads(result['output'])
            actual = output_obj.get('is_vuln', 'no')
        except:
            actual = 'no'
        
        # Confusion matrix
        # Expected: 'yes' = vulnerable, 'no' = safe
        if expected == 'yes':
            if actual == 'yes':
                results_by_prompt[prompt_id]['TP'] += 1
            else:
                results_by_prompt[prompt_id]['FN'] += 1
        else:  # expected == 'no'
            if actual == 'yes':
                results_by_prompt[prompt_id]['FP'] += 1
            else:
                results_by_prompt[prompt_id]['TN'] += 1
    
    # Calculate metrics for each prompt
    metrics = {}
    for prompt_id, counts in results_by_prompt.items():
        tp, fp, tn, fn = counts['TP'], counts['FP'], counts['TN'], counts['FN']
        
        # Precision = TP / (TP + FP)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        
        # Recall = TP / (TP + FN)
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        
        # F1 = 2 * (precision * recall) / (precision + recall)
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        
        metrics[prompt_id] = {
            'TP': tp,
            'FP': fp,
            'TN': tn,
            'FN': fn,
            'Precision': precision,
            'Recall': recall,
            'F1': f1,
            'Accuracy': (tp + tn) / (tp + tn + fp + fn)
        }
    
    return metrics

def write_csv(metrics, output_csv):
    """Write metrics to CSV file."""
    
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow(['Prompt', 'TP', 'FP', 'TN', 'FN', 'Precision', 'Recall', 'F1', 'Accuracy'])
        
        # Data rows
        for prompt_id in sorted(metrics.keys()):
            m = metrics[prompt_id]
            writer.writerow([
                prompt_id,
                m['TP'],
                m['FP'],
                m['TN'],
                m['FN'],
                f"{m['Precision']:.3f}",
                f"{m['Recall']:.3f}",
                f"{m['F1']:.3f}",
                f"{m['Accuracy']:.3f}"
            ])

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 70)
    print("Calculating Lab 2 metrics...")
    print("=" * 70)
    
    results_json = 'reports/lab2_results.json'
    output_csv = 'reports/metrics.csv'
    
    if not os.path.exists(results_json):
        print(f"❌ {results_json} not found!")
        return
    
    metrics = calculate_metrics(results_json)
    write_csv(metrics, output_csv)
    
    # Display results
    print("\nMetrics by Prompt:")
    print("-" * 70)
    for prompt_id in sorted(metrics.keys()):
        m = metrics[prompt_id]
        print(f"\n{prompt_id.upper()}:")
        print(f"  TP: {m['TP']}, FP: {m['FP']}, TN: {m['TN']}, FN: {m['FN']}")
        print(f"  Precision: {m['Precision']:.3f}")
        print(f"  Recall:    {m['Recall']:.3f}")
        print(f"  F1 Score:  {m['F1']:.3f}")
        print(f"  Accuracy:  {m['Accuracy']:.3f}")
    
    print("\n" + "=" * 70)
    print(f"✅ Metrics written to: {output_csv}")
    print("=" * 70)

if __name__ == '__main__':
    main()
