from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

from config import PROCESSED_DATA_DIR


def run(cmd: list[str]) -> None:
    print(">>", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    dataset = PROCESSED_DATA_DIR / "cicids_small.csv"

    print("1) Train teacher")
    run([sys.executable, "-m", "models.train_teacher", "--csv", str(dataset)])

    print("2) Distill student")
    run([sys.executable, "-m", "models.distill_student", "--csv", str(dataset)])

    print("3) Start central server separately with:")
    print("   uvicorn central_server.app:app --reload")

    print("4) Simulate edges with:")
    print(f"   {sys.executable} -m scripts.simulate_edges --csv {dataset} --edge_id edge-1")
    print(f"   {sys.executable} -m scripts.simulate_edges --csv {dataset} --edge_id edge-2")


if __name__ == "__main__":
    main()
