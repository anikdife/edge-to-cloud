from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

from config import LOGS_DIR


LOG_FILE = LOGS_DIR / "events.jsonl"


def append_event(event: Dict[str, Any]) -> None:
    enriched = {
        "timestamp": datetime.utcnow().isoformat(),
        **event,
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(enriched) + "\n")


def summarize_event(event: Dict[str, Any]) -> Dict[str, Any]:
    score = event["inference"]["anomaly_score"]
    severity = "high" if score >= 0.85 else "medium" if score >= 0.6 else "low"

    return {
        "received": True,
        "edge_id": event["edge_id"],
        "severity": severity,
        "score": score,
    }
