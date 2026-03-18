from __future__ import annotations

from pathlib import Path
from models.train_teacher import train_teacher
from models.distill_student import distill_student


def retrain_pipeline(csv_path: Path) -> None:
    print("Retraining teacher...")
    train_teacher(csv_path)
    print("Distilling student...")
    distill_student(csv_path)
    print("Retraining complete.")
