from __future__ import annotations

from pathlib import Path
import pandas as pd

from config import RAW_DATA_DIR, PROCESSED_DATA_DIR, DEFAULT_LABEL_COLUMN, REQUIRED_COLUMNS


def main(input_csv: str, output_csv: str, max_rows: int = 10000) -> None:
    src = Path(input_csv)
    dst = Path(output_csv)

    df = pd.read_csv(src)

    needed = REQUIRED_COLUMNS + [DEFAULT_LABEL_COLUMN]
    missing = [c for c in needed if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df[needed].dropna().head(max_rows)
    dst.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(dst, index=False)

    print(f"Prepared dataset: {dst}")
    print(f"Rows: {len(df)}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--max_rows", type=int, default=10000)
    args = parser.parse_args()

    main(args.input, args.output, args.max_rows)
