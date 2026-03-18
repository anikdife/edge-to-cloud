from __future__ import annotations

import time
import pandas as pd

from edge_agent.capture import sample_record_from_dataframe_row
from edge_agent.infer import EdgeInferencer
from edge_agent.sender import send_to_central


def simulate(csv_path: str, edge_id: str, limit: int = 20, delay: float = 0.5) -> None:
    df = pd.read_csv(csv_path).head(limit)
    inferencer = EdgeInferencer()

    for _, row in df.iterrows():
        flow = sample_record_from_dataframe_row(row.to_dict())
        result = inferencer.predict(flow)
        print(f"[{edge_id}] {result}")
        send_to_central(edge_id, flow, result)
        time.sleep(delay)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--edge_id", required=True)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--delay", type=float, default=0.5)
    args = parser.parse_args()

    simulate(args.csv, args.edge_id, args.limit, args.delay)
