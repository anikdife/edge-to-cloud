from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
OUTPUTS_DIR = BASE_DIR / "outputs"
MODELS_DIR = OUTPUTS_DIR / "models"
LOGS_DIR = OUTPUTS_DIR / "logs"

TEACHER_MODEL_PATH = MODELS_DIR / "teacher_model.joblib"
STUDENT_MODEL_PATH = MODELS_DIR / "student_model.joblib"
SCALER_PATH = MODELS_DIR / "scaler.joblib"
FEATURES_PATH = MODELS_DIR / "feature_columns.joblib"

CENTRAL_SERVER_URL = "http://127.0.0.1:8000"

DEFAULT_LABEL_COLUMN = "label"

REQUIRED_COLUMNS = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets",
    "Fwd Packet Length Mean",
    "Bwd Packet Length Mean",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Packet Length Mean",
    "SYN Flag Count",
    "ACK Flag Count",
    "Destination Port",
]

for path in [RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUTS_DIR, MODELS_DIR, LOGS_DIR]:
    path.mkdir(parents=True, exist_ok=True)
