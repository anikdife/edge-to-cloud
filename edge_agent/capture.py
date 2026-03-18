from __future__ import annotations

import random
from typing import Dict, Any

from config import REQUIRED_COLUMNS


def sample_record_from_dataframe_row(row: dict) -> Dict[str, Any]:
    record = {}
    for col in REQUIRED_COLUMNS:
        record[col] = row[col]
    return record


def generate_synthetic_flow() -> Dict[str, Any]:
    return {
        "Flow Duration": random.randint(1000, 500000),
        "Total Fwd Packets": random.randint(1, 200),
        "Total Backward Packets": random.randint(0, 180),
        "Total Length of Fwd Packets": random.uniform(100, 50000),
        "Total Length of Bwd Packets": random.uniform(0, 45000),
        "Fwd Packet Length Mean": random.uniform(20, 1200),
        "Bwd Packet Length Mean": random.uniform(0, 1200),
        "Flow Bytes/s": random.uniform(1, 100000),
        "Flow Packets/s": random.uniform(0.1, 5000),
        "Packet Length Mean": random.uniform(20, 1500),
        "SYN Flag Count": random.randint(0, 10),
        "ACK Flag Count": random.randint(0, 30),
        "Destination Port": random.choice([80, 443, 53, 22, 21, 8080, 3389]),
    }
