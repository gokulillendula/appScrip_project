# 📊 Market Analysis API (FastAPI + Gemini)

## 🚀 Overview

This project is a FastAPI-based backend service that analyzes market data for different sectors in India and generates structured **markdown reports** with trade opportunities.

The system collects recent news data, processes it using an AI model (Google Gemini), and returns a well-structured market analysis report.

---

## 🎯 Features

* 🔍 **Sector-based Analysis**

  * Analyze sectors like `pharmaceuticals`, `technology`, `agriculture`, etc.

* 🌐 **Real-time Data Collection**

  * Fetches latest news using DuckDuckGo Search (DDGS)

* 🤖 **AI-Powered Insights**

  * Uses Google Gemini API to generate structured analysis

* 📝 **Markdown Output**

  * Returns clean markdown reports that can be saved as `.md` files

* 🔐 **Authentication**

  * HTTP Basic Authentication (username & password)

* 🚦 **Rate Limiting**

  * Limits API usage per user (5 requests/minute)

* 📊 **Session Management**

  * Tracks user activity and request count

* 🛡️ **Input Validation**

  * Validates sector names to prevent invalid inputs

* 📜 **Logging**

  * Logs API requests and errors for monitoring

---

## 🧱 Tech Stack

* **Backend:** FastAPI
* **Server:** Uvicorn
* **AI Model:** Google Gemini API
* **Data Source:** DuckDuckGo Search (DDGS)
* **Language:** Python

---

## 📁 Project Structure

```
project/
│
├── main.py              # FastAPI app and endpoints
├── llm.py               # Gemini AI integration
├── scraper.py           # News fetching logic
├── auth.py              # Authentication logic
├── rate_limiter.py      # Rate limiting
├── session.py           # Session tracking
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/gokulillendula/appScrip_project.git
cd appScrip_project
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the application

```
uvicorn main:app --reload
```

---

## 🌐 API Usage

### Endpoint

```
GET /analyze/{sector}
```

### Example

```
/analyze/pharmaceuticals
```

---

## 🔐 Authentication

This API uses **HTTP Basic Authentication**

### Credentials:

```
Username: admin
Password: 1234
```

---

## 📄 Sample Output (Markdown)

```
# Pharmaceutical Sector Analysis (India)

## Overview
...

## Key Trends
- ...

## Opportunities
- ...

## Risks
- ...

## Trade Opportunities
- ...

## Conclusion
...
```

---

## 🚦 Rate Limiting

* Max **5 requests per minute per user**
* Returns `429 Too Many Requests` if exceeded

---

## ⚠️ Error Handling

* Handles API failures (Gemini)
* Handles data fetching errors
* Returns meaningful responses instead of crashing

---

## 📊 Logging

* Logs user requests
* Logs errors for debugging

---

## 🚀 Deployment

The project can be deployed on:

* Render
* Railway

Example start command:

```
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## 🧠 Design Decisions

* Used **Basic Auth** for simplicity and security
* Used **in-memory storage** for sessions and rate limiting
* Limited news results (5–10) for better AI accuracy
* Used **markdown output** for readability and portability

---

## 🔮 Future Improvements

* Add database (Redis/PostgreSQL)
* Improve caching
* Add async scraping
* Support multiple users
* Enhance prompt engineering

---

## 👨‍💻 Author

**Gokul Illendula**

---

## ✅ Conclusion

This project demonstrates:

* FastAPI backend development
* AI integration
* Data collection & processing
* Security implementation
* Clean API design

---
