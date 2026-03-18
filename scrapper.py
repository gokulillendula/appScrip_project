
from duckduckgo_search import DDGS

def get_news(sector:str):
    query=f"{sector} sector india latest news"
    results=[]
    with DDGS() as ddgs:
        news=ddgs.news(query,region="in-en",timelimit="7d",max_results=8)
        for item in news:
            results.append({
                "title":item["title"],
                "summary": item["body"],
                "url": item["url"],
                "date": item["date"]
            })
    return results