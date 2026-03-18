from __future__ import annotations

from typing import Dict, Any
import requests

from config import CENTRAL_SERVER_URL


def send_to_central(edge_id: str, flow_record: Dict[str, Any], inference: Dict[str, Any]) -> None:
    payload = {
        "edge_id": edge_id,
        "flow_record": flow_record,
        "inference": inference,
    }

    response = requests.post(f"{CENTRAL_SERVER_URL}/ingest", json=payload, timeout=10)
    response.raise_for_status()
    print(f"[{edge_id}] sent -> {response.json()}")
