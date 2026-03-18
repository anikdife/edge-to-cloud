from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from fastapi import FastAPI
from pydantic import BaseModel

from central_server.aggregator import append_event, summarize_event
from central_server.retrain import retrain_pipeline

app = FastAPI(title="Distributed IDS Central Server")


class IngestRequest(BaseModel):
    edge_id: str
    flow_record: Dict[str, float | int]
    inference: Dict[str, float | int | str]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ingest")
def ingest(req: IngestRequest):
    data = req.model_dump()
    append_event(data)
    return summarize_event(data)


@app.post("/retrain")
def retrain(payload: Dict[str, str]):
    csv_path = Path(payload["csv_path"])
    retrain_pipeline(csv_path)
    return {"status": "retrained", "csv_path": str(csv_path)}
