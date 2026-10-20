#!/usr/bin/env python3
"""Run mutation testing and enforce the configured score threshold."""

import argparse
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "setup.cfg"
CACHE = ROOT / "mutants"
THRESHOLD_FILE = ROOT / ".mutation-threshold"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", choices=("strong", "weak"), default="strong")
    parser.add_argument("--expect-below", action="store_true")
    args = parser.parse_args()

    suite = args.suite
    threshold = int(THRESHOLD_FILE.read_text().strip())

    previous_config = CONFIG.read_text() if CONFIG.exists() else None
    CONFIG.write_text(
        "[mutmut]\n"
        "source_paths=core\n"
        f"pytest_add_cli_args_test_selection=tests/{suite}\n"
    )

    try:
        shutil.rmtree(CACHE, ignore_errors=True)
        result = subprocess.run(
            ["mutmut", "run"],
            cwd=ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print(result.stdout, end="")

        if result.returncode != 0:
            print(f"\nERROR: Mutmut exited with status {result.returncode}.")
            return result.returncode

        summaries = re.findall(
            r"(\d+)/(\d+)\s+🎉\s+(\d+).*?🙁\s+(\d+)",
            result.stdout,
        )
        if not summaries:
            print("\nERROR: Could not parse Mutmut's score summary.")
            return 2

        _, total_text, killed_text, survived_text = summaries[-1]
        total = int(total_text)
        killed = int(killed_text)
        survived = int(survived_text)
        denominator = killed + survived

        if denominator == 0:
            print("ERROR: No scored mutants were reported.")
            return 2

        score = killed / denominator * 100
        below = score < threshold

        print(f"\nSuite: {suite}")
        print(f"Mutants processed: {total}")
        print(f"Killed: {killed}; surviving: {survived}")
        print(f"Mutation score: {score:.1f}%")
        print(f"Required threshold: {threshold}%")

        if args.expect_below:
            if below:
                print("QUALITY GATE: PASS (expected below-threshold score)")
                return 0
            print("QUALITY GATE: FAIL (expected score below threshold)")
            return 1

        if below:
            print("QUALITY GATE: FAIL")
            return 1

        print("QUALITY GATE: PASS")
        return 0
    finally:
        if previous_config is None:
            CONFIG.unlink(missing_ok=True)
        else:
            CONFIG.write_text(previous_config)


if __name__ == "__main__":
    raise SystemExit(main())