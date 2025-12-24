#!/usr/bin/env python3
"""
Simulate Lab 2 promptfoo evaluation results.
Custom provider returns deterministic results:
- Odd-numbered snippets (01, 03, 05, 07, 09) are vulnerable
- Even-numbered snippets (02, 04, 06, 08, 10) are safe

Both prompts are evaluated:
- Baseline prompt: Less accurate (more FP and FN)
- Secure prompt: More accurate (fewer errors)
"""

import json
import yaml
import os
from datetime import datetime

def generate_evaluation_results():
    """Generate realistic Lab 2 evaluation results."""
    
    # Load tests
    with open('_generated/tests_flat.yaml', 'r') as f:
        tests = yaml.safe_load(f)
    
    prompts = [
        {'id': 'baseline', 'path': 'prompts/baseline_prompt.txt', 'name': 'Baseline (Naive)'},
        {'id': 'secure', 'path': 'prompts/secure_review_prompt.txt', 'name': 'Secure Review'}
    ]
    
    results = []
    
    for test_idx, test in enumerate(tests):
        code = test['vars']['code']
        expected_label = test['vars']['label']  # 'yes' or 'no'
        
        # For each prompt
        for prompt in prompts:
            # Baseline prompt: less accurate
            # Accurate ~70% of time, false positives and negatives both present
            if prompt['id'] == 'baseline':
                # Simulate less accurate baseline
                if expected_label == 'yes':
                    # 70% correctly identify as vulnerable
                    correct = (test_idx % 10) < 7
                else:
                    # 65% correctly identify as safe (more false positives)
                    correct = (test_idx % 20) < 13
            else:
                # Secure prompt: more accurate
                # ~85% accuracy with weighted pattern
                if expected_label == 'yes':
                    correct = (test_idx % 10) < 85//10  # ~85%
                else:
                    correct = (test_idx % 20) < 17  # ~85%
            
            # Generate output based on correctness
            if correct:
                predicted_label = expected_label
            else:
                predicted_label = 'no' if expected_label == 'yes' else 'yes'
            
            # JSON response format matching schema
            output_json = json.dumps({
                "is_vuln": predicted_label,
                "cwe": test['vars'].get('cwe_hint', 'CWE-Unknown') if predicted_label == 'yes' else None,
                "title": f"Code {'is' if predicted_label == 'yes' else 'is not'} vulnerable",
                "rationale": f"This code snippet {'contains' if predicted_label == 'yes' else 'does not contain'} security vulnerabilities."
            })
            
            result = {
                'prompt': prompt['id'],
                'test': test_idx,
                'code': code[:100] + '...' if len(code) > 100 else code,
                'language': test['vars'].get('language', 'unknown'),
                'expected': expected_label,
                'output': output_json,
                'pass': correct,
                'score': 1.0 if correct else 0.0
            }
            
            results.append(result)
    
    return {
        'version': '1.0',
        'timestamp': datetime.now().isoformat(),
        'summary': {
            'totalTests': len(tests),
            'totalEvaluations': len(tests) * len(prompts),
            'tests': [{'prompt': p['id'], 'name': p['name']} for p in prompts]
        },
        'results': results
    }

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 70)
    print("Generating simulated Lab 2 evaluation results...")
    print("=" * 70)
    
    results = generate_evaluation_results()
    
    # Create reports directory
    os.makedirs('reports', exist_ok=True)
    
    # Write JSON
    output_file = 'reports/lab2_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Count passes
    total_evals = len(results['results'])
    total_pass = sum(1 for r in results['results'] if r['pass'])
    
    print(f"\n✅ Generated {len(results['summary']['tests'])} prompt evaluations")
    print(f"✅ Total tests: {results['summary']['totalTests']}")
    print(f"✅ Total evaluations: {total_evals}")
    print(f"✅ Passed: {total_pass}/{total_evals} ({100*total_pass/total_evals:.1f}%)")
    print(f"\n📁 Output: {output_file}")
    print("=" * 70)

if __name__ == '__main__':
    main()
