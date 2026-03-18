from __future__ import annotations

from typing import Dict, Any

import joblib
import pandas as pd

from config import STUDENT_MODEL_PATH, SCALER_PATH, FEATURES_PATH


class EdgeInferencer:
    def __init__(self) -> None:
        self.model = joblib.load(STUDENT_MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)
        self.features = joblib.load(FEATURES_PATH)

    def predict(self, flow_record: Dict[str, Any]) -> Dict[str, Any]:
        row = pd.DataFrame([flow_record])[self.features]
        row_scaled = self.scaler.transform(row)

        pred = int(self.model.predict(row_scaled)[0])
        prob = float(self.model.predict_proba(row_scaled)[0][1])

        return {
            "prediction": pred,
            "anomaly_score": round(prob, 6),
            "label_name": "attack" if pred == 1 else "benign",
        }
