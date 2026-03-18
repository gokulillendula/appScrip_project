import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
def generate_analysis(sector:str, news:list):
    api_key=os.getenv("api_key")
    genai.configure(api_key=api_key)
    combined_text=""
    for i, article in enumerate(news,1):
        combined_text += f"""
        News {i}:
        Title: {article['title']}
        Summary: {article['summary']}
        Date: {article['date']}
        """
    prompt = f"""
You are a financial analyst.

Analyze the {sector} sector in India using the following news:

{combined_text}

Return STRICTLY in markdown format.

Structure:

# {sector.capitalize()} Sector Analysis (India)

## Overview
## Key Trends
## Opportunities
## Risks
## Trade Opportunities
## Conclusion

Use bullet points where necessary.
Do not add anything outside markdown.
"""
    model=genai.GenerativeModel("gemini-2.5-flash")
    response=model.generate_content(prompt)
    return  response.text