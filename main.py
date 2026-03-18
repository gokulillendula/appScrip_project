from fastapi import FastAPI,Depends
from scrapper import get_news
from fastapi.responses import PlainTextResponse
from llm import generate_analysis
from fastapi import HTTPException
from auth import verify_user
from rate_limit import check_rate_limit
import logging


app=FastAPI()
sessions = {}
def track_session(user: str):
    import time

    if user not in sessions:
        sessions[user] = {
            "count": 0,
            "last_request": None
        }

    sessions[user]["count"] += 1
    sessions[user]["last_request"] = time.time()


def validate_sector(sector: str):
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Sector must contain only letters")

    if len(sector) < 3:
        raise HTTPException(status_code=400, detail="Sector name too short")

    return sector

@app.get("/analyze/{sector}",response_class=PlainTextResponse)

def analyze(sector:str,user: str = Depends(verify_user)):
    logging.basicConfig(level=logging.INFO)

    logging.info(f"Request received for sector: {sector}")
    check_rate_limit(user)
    track_session(user)
    sector = validate_sector(sector)
    news_data=get_news(sector)
    if not news_data:
        return "No news found for the specified sector."
    try:
        markdown_report = generate_analysis(sector, news_data)
    except Exception:
        markdown_report = "AI service unavailable. Try again later."

    return markdown_report