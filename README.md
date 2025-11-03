# 🇰🇪 Mobile Lending Risk API - Kenya

## Problem Definition

Across Kenya, mobile lending has become the everyday bank for millions — fast, digital, and accessible through a few taps. But while lending has gone mobile, risk assessment hasn’t kept up. Many platforms still depend on outdated rules or guesswork, leading to poor credit decisions, high defaults, and unfair loan rejections.

This project builds a smarter alternative: a machine-learning API that reads real financial behavior — especially M-PESA transactions — to instantly predict a borrower’s credit risk. It gives lenders a data-driven, explainable, and human-centered way to decide who gets credit, creating a more inclusive and transparent digital lending ecosystem for Kenya.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)

ML-powered credit scoring API for mobile lending in Kenya with M-PESA integration.

##  Live Demo

**API**: [Will be added after deployment]  
**Docs**: [Will be added after deployment]/docs

## Features

- ✅ Real-time credit risk prediction
- ✅ M-PESA transaction analysis
- ✅ REST API with automatic documentation
- ✅ Kenya-specific features

## Quick Start

### Local Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run API
cd api
uvicorn main:app --reload
```

Visit: http://localhost:8000/docs

### Test API
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 32,
    "monthly_income": 45000,
    "loan_amount": 50000,
    "loan_term_months": 12,
    "existing_loans": 1,
    "previous_defaults": 0,
    "employment_status": "employed",
    "education_level": "university",
    "dependents": 2,
    "mpesa_transactions_monthly": 45,
    "mpesa_average_balance": 15000,
    "mpesa_savings_rate": 0.15
  }'
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information |
| `/health` | GET | Health check |
| `/predict` | POST | Score loan applicant |

## Example Response
```json
{
  "applicant_id": "APP20250117123045",
  "default_probability": 0.1234,
  "risk_category": "LOW",
  "recommendation": "APPROVE - Low risk applicant",
  "score": 782,
  "timestamp": "2025-01-17T12:30:45"
}
```

## Technology Stack

- **Backend**: FastAPI, Python
- **ML**: scikit-learn, XGBoost
- **Deployment**: Render
- **Data**: Pandas, NumPy

## Project Structure
```
mobile-lending-risk-kenya/
├── api/
│   └── main.py          # FastAPI application
├── data/                # Data files
├── models/              # Saved models
├── notebooks/           # Jupyter notebooks
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Future Enhancements

- [ ] Train ML models on real data
- [ ] Add model interpretability (SHAP)
- [ ] Create frontend dashboard
- [ ] Add authentication
- [ ] Deploy monitoring

## Author

Your Name - [GitHub](https://github.com/EmmanuelOchieng01) | [LinkedIn](https://linkedin.com/in/yourprofile)

## License

MIT License
```

---

#### **File 4: `.gitignore`** (in root folder)
```
# Python
__pycache__/
*.py[cod]
venv/
env/

# Data
*.csv
*.xlsx
*.pkl

# IDE
.vscode/
.idea/

# OS

.DS_Store

