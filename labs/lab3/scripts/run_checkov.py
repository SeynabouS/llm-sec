#!/usr/bin/env python3
import json, subprocess, argparse, sys, os
from pathlib import Path

root = Path(__file__).resolve().parent.parent
reports = root / "reports"
reports.mkdir(exist_ok=True)


def build_cmd():
    default_dirs = [root / "terraform", root / "k8s", root / "docker"]
    dirs_env = os.environ.get("CHECKOV_DIRS", "").strip()
    if dirs_env:
        raw_dirs = dirs_env.replace(",", os.pathsep).split(os.pathsep)
        targets = []
        for raw_dir in raw_dirs:
            raw_dir = raw_dir.strip()
            if not raw_dir:
                continue
            path = Path(raw_dir)
            if not path.is_absolute():
                path = root / path
            targets.append(path)
    else:
        targets = default_dirs
    output = os.environ.get("CHECKOV_OUTPUT", "json").strip().lower()
    if output not in {"json", "sarif"}:
        output = "json"
    cmd = ["checkov"]
    for target in targets:
        cmd.extend(["-d", str(target)])
    cmd.extend(["--output", output])
    return cmd


def run(after: bool = False, *, runner=subprocess.run, report_dir: Path = reports) -> Path:
    out = report_dir / ("checkov_after.json" if after else "checkov.json")
    try:
        cmd = build_cmd()
        if runner is subprocess.run and os.name == "nt":
            venv_dir = str(Path(sys.executable).parent)
            env = os.environ.copy()
            env["PATH"] = venv_dir + os.pathsep + env.get("PATH", "")
            cmd = ["cmd", "/c"] + cmd
            res = runner(cmd, capture_output=True, text=True, check=False, env=env)
        else:
            res = runner(cmd, capture_output=True, text=True, check=False)
        text = res.stdout.strip()
        out.write_text(text, encoding="utf-8")
        print(f"Wrote {out}")
        if res.returncode not in (0, 1):
            print(f"checkov exit code {res.returncode}: see stderr below", file=sys.stderr)
            print(res.stderr, file=sys.stderr)
    except FileNotFoundError:
        print("Checkov not found. Install with: pip install checkov", file=sys.stderr)
        sys.exit(2)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--after", action="store_true", help="Write *_after.json")
    args = parser.parse_args()
    run(after=args.after)


if __name__ == "__main__":
    main()
