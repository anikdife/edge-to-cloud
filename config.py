from __future__ import annotations

from pathlib import Path
from typing import Tuple, List

import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from config import (
    DEFAULT_LABEL_COLUMN,
    FEATURES_PATH,
    SCALER_PATH,
    REQUIRED_COLUMNS,
)


def normalize_label(value: str) -> int:
    v = str(value).strip().lower()
    return 0 if v == "benign" else 1


def load_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    missing = [c for c in REQUIRED_COLUMNS + [DEFAULT_LABEL_COLUMN] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df


def preprocess_dataframe(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    work = df[REQUIRED_COLUMNS + [DEFAULT_LABEL_COLUMN]].copy()

    for col in REQUIRED_COLUMNS:
        work[col] = pd.to_numeric(work[col], errors="coerce")

    work = work.dropna()
    y = work[DEFAULT_LABEL_COLUMN].apply(normalize_label)
    X = work[REQUIRED_COLUMNS]
    return X, y


def fit_scaler(X_train: pd.DataFrame) -> StandardScaler:
    scaler = StandardScaler()
    scaler.fit(X_train)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(list(X_train.columns), FEATURES_PATH)
    return scaler


def load_scaler() -> StandardScaler:
    return joblib.load(SCALER_PATH)


def load_feature_columns() -> List[str]:
    return joblib.load(FEATURES_PATH)


def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42,
):
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
