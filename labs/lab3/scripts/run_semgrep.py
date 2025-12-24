#!/usr/bin/env python3
import json, subprocess, argparse, sys, os
from pathlib import Path

root = Path(__file__).resolve().parent.parent
reports = root / "reports"
reports.mkdir(exist_ok=True)


def build_cmd():
    configs = []
    targets = []
    k8s_dir = root / "k8s"
    if k8s_dir.exists():
        configs.extend(["--config", "p/kubernetes"])
        targets.append(str(k8s_dir))
    docker_dir = root / "docker"
    if docker_dir.exists():
        configs.extend(["--config", "p/dockerfile"])
        targets.append(str(docker_dir))
    terraform_dir = root / "terraform"
    if terraform_dir.exists():
        configs.extend(["--config", "p/terraform"])
        targets.append(str(terraform_dir))
    local_rules = root / "config" / "semgrep_rules.yml"
    if local_rules.exists():
        configs.extend(["--config", str(local_rules)])
    if not targets:
        targets.append(str(root))
    cmd = ["semgrep", *configs, "--json", *targets]
    return cmd


def run(after: bool = False, *, runner=subprocess.run, report_dir: Path = reports) -> Path:
    out = report_dir / ("semgrep_after.json" if after else "semgrep.json")
    try:
        cmd = build_cmd()
        if runner is subprocess.run and os.name == "nt":
            venv_dir = str(Path(sys.executable).parent)
            env = os.environ.copy()
            env["PATH"] = venv_dir + os.pathsep + env.get("PATH", "")
            cmd = ["cmd", "/c"] + cmd
            res = runner(
                cmd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
                env=env,
            )
        else:
            res = runner(cmd, capture_output=True, text=True, check=False)
        text = res.stdout.strip()
        out.write_text(text, encoding="utf-8")
        print(f"Wrote {out}")
        if res.returncode not in (0, 1):
            print(f"semgrep exit code {res.returncode}: see stderr below", file=sys.stderr)
            print(res.stderr, file=sys.stderr)
    except FileNotFoundError:
        print("Semgrep not found. Install with: pip install semgrep", file=sys.stderr)
        sys.exit(2)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--after", action="store_true", help="Write *_after.json")
    args = parser.parse_args()
    run(after=args.after)


if __name__ == "__main__":
    main()
