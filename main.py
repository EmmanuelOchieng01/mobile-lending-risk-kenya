from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import pandas as pd
import numpy as np
from datetime import datetime

app = FastAPI(title="Mobile Lending Risk API", version="1.0.0")

class ApplicantData(BaseModel):
    age: int
    monthly_income: float
    loan_amount: float
    loan_term_months: int
    existing_loans: int = 0
    previous_defaults: int = 0
    employment_status: str
    education_level: str
    dependents: int = 0
    mpesa_transactions_monthly: int = 0
    mpesa_average_balance: float = 0
    mpesa_savings_rate: float = 0
    credit_history_length: int = 0
    previous_loans: int = 0
    days_since_last_loan: int = 365

class PredictionResponse(BaseModel):
    applicant_id: str
    default_probability: float
    risk_category: str
    recommendation: str
    score: int
    timestamp: str

@app.get("/")
def root():
    return {
        "message": "Mobile Lending Risk API - Kenya",
        "status": "active",
        "endpoints": ["/predict", "/health"]
    }

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/predict", response_model=PredictionResponse)
def predict(applicant: ApplicantData):
    # Simple rule-based scoring
    risk_score = 0
    
    # Risk factors
    if applicant.loan_amount / applicant.monthly_income > 3:
        risk_score += 0.2
    if applicant.previous_defaults > 0:
        risk_score += 0.3
    if applicant.age < 25:
        risk_score += 0.15
    if applicant.existing_loans > 2:
        risk_score += 0.1
    if applicant.mpesa_transactions_monthly < 10:
        risk_score += 0.1
    
    # Protective factors
    if applicant.monthly_income > 50000:
        risk_score -= 0.1
    if applicant.mpesa_savings_rate > 0.15:
        risk_score -= 0.1
    if applicant.credit_history_length > 24:
        risk_score -= 0.08
    
    default_prob = max(0.05, min(0.95, risk_score))
    
    # Risk category
    if default_prob < 0.2:
        risk_cat = "LOW"
        recommendation = "APPROVE - Low risk applicant"
    elif default_prob < 0.4:
        risk_cat = "MEDIUM"
        recommendation = "REVIEW - Moderate risk"
    elif default_prob < 0.6:
        risk_cat = "HIGH"
        recommendation = "CAUTION - High risk"
    else:
        risk_cat = "VERY HIGH"
        recommendation = "REJECT - Very high risk"
    
    credit_score = int(850 - (default_prob * 550))
    
    return PredictionResponse(
        applicant_id=f"APP{datetime.now().strftime('%Y%m%d%H%M%S')}",
        default_probability=round(default_prob, 4),
        risk_category=risk_cat,
        recommendation=recommendation,
        score=credit_score,
        timestamp=datetime.now().isoformat()
    )