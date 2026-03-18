from __future__ import annotations

import json
from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

from config import TEACHER_MODEL_PATH
from models.utils import load_dataset, preprocess_dataframe, split_data, fit_scaler


def train_teacher(csv_path: Path) -> None:
    df = load_dataset(csv_path)
    X, y = preprocess_dataframe(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    scaler = fit_scaler(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=12,
        min_samples_split=4,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced",
    )
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    print("=== Teacher Model Report ===")
    print(classification_report(y_test, y_pred, digits=4))
    print("ROC-AUC:", round(roc_auc_score(y_test, y_prob), 4))

    joblib.dump(model, TEACHER_MODEL_PATH)
    print(f"Saved teacher model to: {TEACHER_MODEL_PATH}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Path to training CSV")
    args = parser.parse_args()

    train_teacher(Path(args.csv))
