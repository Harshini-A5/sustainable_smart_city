from fastapi import APIRouter, UploadFile, File
import pandas as pd
from app.utils.anomaly_file_checker import detect_anomalies

router = APIRouter()

@router.post("/check-anomalies")
async def check_anomalies(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(pd.compat.StringIO(contents.decode("utf-8")))
    anomalies = detect_anomalies(df)
    return {"anomalies": anomalies}
