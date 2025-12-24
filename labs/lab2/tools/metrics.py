import json, sys, csv

def main(inp, out_csv):
    with open(inp, encoding="utf-8") as f:
        data = json.load(f)
    # promptfoo v3 JSON: results, prompts, outputs vary by version; handle table fallback
    # We expect 'results' with evals; fallback to 'table' older format.
    # Handle nested structure: data['results']['results'] or data['results']
    results_container = data.get("results") or {}
    if isinstance(results_container, dict):
        results = results_container.get("results") or []
    else:
        results = results_container
    table = data.get("table")
    if not results and not table:
        raise SystemExit("Unrecognized results format")
    # Collect rows with: promptIdx, vars.label, output JSON is_vuln
    rows = []
    if results:
        # v3 style: results[i] has 'response' (raw text or dict), 'vars', 'promptIdx'
        for r in results:
            promptIdx = r.get("promptIdx", 0)
            vars_ = r.get("vars", {})
            label = (vars_.get("label") or "").lower()
            
            # Handle different output formats: response (string or dict), output, text
            response = r.get("response")
            if isinstance(response, dict):
                out = response.get("output", "")
            elif isinstance(response, str):
                out = response
            else:
                out = r.get("output", "") or r.get("text", "")
            
            try:
                obj = json.loads(out) if isinstance(out, str) else out
                pred = (obj.get("is_vuln","") or "").lower()
            except Exception:
                pred = "error"
            rows.append((promptIdx, label, pred))
    else:
        # table style
        head_prompts = table["head"]["prompts"]
        for body in table["body"]:
            vars_ = {k:v for k,v in zip(table["head"]["vars"], body["vars"])}
            label = (vars_.get("label") or "").lower()
            for i, out in enumerate(body["outputs"]):
                text = out.get("text","")
                try:
                    obj = json.loads(text)
                    pred = (obj.get("is_vuln","") or "").lower()
                except Exception:
                    pred = "error"
                rows.append((i, label, pred))

    # Compute metrics per promptIdx
    from collections import defaultdict
    counts = defaultdict(lambda: {"tp":0,"fp":0,"tn":0,"fn":0,"errors":0})
    for pidx, label, pred in rows:
        if pred == "error":
            counts[pidx]["errors"] += 1
            continue
        # Normalize to yes/no
        pred_bin = "yes" if pred == "yes" else "no"
        if label == "yes":
            if pred_bin == "yes": counts[pidx]["tp"] += 1
            else: counts[pidx]["fn"] += 1
        else:
            if pred_bin == "yes": counts[pidx]["fp"] += 1
            else: counts[pidx]["tn"] += 1

    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["promptIdx","TP","FP","TN","FN","Errors","Precision","Recall","F1"])
        for pidx, c in sorted(counts.items()):
            tp, fp, tn, fn, err = c["tp"], c["fp"], c["tn"], c["fn"], c["errors"]
            prec = tp/(tp+fp) if (tp+fp)>0 else 0.0
            rec = tp/(tp+fn) if (tp+fn)>0 else 0.0
            f1 = 2*prec*rec/(prec+rec) if (prec+rec)>0 else 0.0
            w.writerow([pidx,tp,fp,tn,fn,err,f"{prec:.3f}",f"{rec:.3f}",f"{f1:.3f}"])
    print(f"Wrote {out_csv}")

if __name__ == "__main__":
    if len(sys.argv)<3:
        print("Usage: python tools/metrics.py results.json metrics.csv")
        raise SystemExit(2)
    main(sys.argv[1], sys.argv[2])
