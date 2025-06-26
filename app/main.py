"""# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat_router, feedback_router, policy_router, kpi_upload_router, anomaly_checker

app = FastAPI(title="Sustainable Smart City Assistant")

# CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(chat_router.router, prefix="/chat", tags=["Chat"])
app.include_router(feedback_router.router, prefix="/feedback", tags=["Feedback"])
app.include_router(policy_router.router, prefix="/policy", tags=["Policy Summarizer"])
app.include_router(kpi_upload_router.router, prefix="/kpi", tags=["KPI Forecast"])
app.include_router(anomaly_checker.router, prefix="/anomaly", tags=["Anomaly Checker"])

@app.get("/")
def read_root():
    return {"message": "Sustainable Smart City Assistant is running..."}"""
from fastapi import FastAPI
from app.api import chat_router, feedback_router, eco_tips_router, policy_router, report_router, vector_router, kpi_upload_router
from app.api import eco_tips_router
from app.api import report_router

app = FastAPI()

app.include_router(chat_router.router, prefix="/chat")
app.include_router(feedback_router.router, prefix="/feedback")
app.include_router(chat_router.router, prefix="/chat")
app.include_router(feedback_router.router, prefix="/feedback")
app.include_router(eco_tips_router.router, prefix="/eco-tips")
app.include_router(policy_router.router, prefix="/policy")
app.include_router(report_router.router, prefix="/report")
app.include_router(vector_router.router, prefix="/vector")
app.include_router(kpi_upload_router.router, prefix="/kpi")
app.include_router(eco_tips_router.router)
app.include_router(report_router.router)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Sustainable Smart City Assistant is running!"}
