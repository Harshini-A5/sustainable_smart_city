from fastapi import APIRouter, UploadFile, File
import pandas as pd
#from app.utils.kpi_file_forecaster import forecast_kpi
from app.utils.helpers import save_uploaded_file, log_event




router = APIRouter()

@router.post("/upload-kpi")
async def upload_kpi_file(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(pd.compat.StringIO(contents.decode("utf-8")))
    forecast = forecast_kpi(df)
    return {"forecast": forecast}
