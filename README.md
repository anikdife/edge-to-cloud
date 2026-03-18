# Distributed Flow-Based IDS (Prototype)

A prototype for a distributed intrusion detection system aligned with edge-to-cloud cyber defense research.

## Research idea

This project simulates a lightweight distributed IDS architecture:

- **Distributed Guard (DG):** edge agents perform local inference using compact student models
- **Good Nexus (GN):** central node receives anomaly reports, aggregates events, and retrains models

The prototype focuses on:

- flow-based / metadata-based detection
- encrypted-traffic-compatible features
- teacher-student distillation
- distributed reporting from edge nodes to a central server

---

## Tech stack

- Python
- scikit-learn
- FastAPI
- pandas
- joblib

---

## Project structure

```text
edge_agent/        edge-side feature reading + inference + sending
central_server/    API server + aggregation + retraining
models/            teacher/student training code
scripts/           data prep + multi-edge simulation
outputs/           saved models and logs
