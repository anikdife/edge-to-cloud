from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

from config import TEACHER_MODEL_PATH, STUDENT_MODEL_PATH
from models.utils import load_dataset, preprocess_dataframe, split_data, load_scaler


def distill_student(csv_path: Path) -> None:
    teacher = joblib.load(TEACHER_MODEL_PATH)

    df = load_dataset(csv_path)
    X, y = preprocess_dataframe(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    scaler = load_scaler()
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    teacher_soft = teacher.predict_proba(X_train_scaled)[:, 1]
    pseudo_y = (teacher_soft >= 0.5).astype(int)

    student = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42,
    )
    student.fit(X_train_scaled, pseudo_y)

    y_pred = student.predict(X_test_scaled)
    y_prob = student.predict_proba(X_test_scaled)[:, 1]

    print("=== Student Model Report ===")
    print(classification_report(y_test, y_pred, digits=4))
    print("ROC-AUC:", round(roc_auc_score(y_test, y_prob), 4))

    joblib.dump(student, STUDENT_MODEL_PATH)
    print(f"Saved student model to: {STUDENT_MODEL_PATH}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Path to training CSV")
    args = parser.parse_args()

    distill_student(Path(args.csv))
