"""One-command rebuild (bonus task).
Runs: Stage 1 ingestion, Stages 2-4 build, Stage 5 queries, Stage 6 DQ, presentation assets.
Requires: dataset files in data/ (see README.md).
"""
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

STEPS = [
    ["python3", str(BASE / "ingestion" / "load_raw.py")],
    ["python3", str(BASE / "transform" / "build_pipeline.py")],
    ["python3", str(BASE / "analytics" / "run_queries.py")],
    ["python3", str(BASE / "quality" / "dq_checks.py")],
    ["python3", str(BASE / "presentation" / "make_assets.py")],
]

def main():
    for step in STEPS:
        print(f"\n=== {' '.join(step)} ===")
        r = subprocess.run(step, check=False)
        if r.returncode != 0:
            print(f"FAILED: {' '.join(step)} (exit {r.returncode})", file=sys.stderr)
            return r.returncode
    print("\nPipeline complete. See analytics/results/, dq_results, presentation/.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
