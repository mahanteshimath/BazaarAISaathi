# BazaarAISaathi
Your AI Friend in the Stock Market 🤖📈

## Overview
BazaarAISaathi is an innovative, AI-powered platform that empowers investors with deep insights into the Indian stock market. By combining advanced natural language processing, real-time data analytics, and expert-driven financial modeling, the app provides personalized investment strategies, market sentiment analyses, and portfolio optimization recommendations.

## Features
- **Financial Independence Planner (FIRE):** Generate detailed, personalized plans to achieve financial independence with inputs like age, salary, marital status, and more.
- **Investment Advice Tester:** Submit investment tips via text or image; the app extracts text (using EasyOCR) and delivers AI-powered deep analysis.
- **Fundamental & Technical Analysis:** Access comprehensive reports on company fundamentals, market sentiment, and trading strategies.
- **Portfolio Analysis:** Upload or paste your portfolio for multi-dimensional analysis and stock-wise recommendations.
- **Market Research & Competitor Benchmarking:** Leverage AI-driven research to assess industry trends, compare competitors, and identify new opportunities.
- **Deep Market Insights:** Stay updated with real-time indicators like top gainers/losers, macro-economic trends, and critical market data.

## Technologies Used
- **Streamlit:** For building a responsive, interactive web app.
- **Perplexity AI & LangChain:** To power advanced natural language processing and financial forecasting.
- **Pandas, Plotly & BeautifulSoup:** For data manipulation and visualization.
- **EasyOCR & Docling Parse:** For efficient, pure-Python text extraction from images and PDFs.
- **Python Ecosystem:** Including requests, python-dotenv, and more.

## Hackathon Highlights
- **Cutting-Edge Innovation:** Integrates multiple AI models for end-to-end financial advice.
- **User-Centric Design:** Intuitive interfaces across modules like FIRE planning, tip testing, and market analysis.
- **Scalable Architecture:** Modular code structure that supports future feature expansion.
- **Real-Time Insights:** Combines live market data with historical trends to deliver timely investment recommendations.

## Installation & Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/BazaarAISaathi.git
   cd BazaarAISaathi
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API Keys:**
   - Set up your Streamlit secrets and API keys (Perplexity, etc.) in a `secrets.toml` file.
4. **Run the App:**
   ```bash
   streamlit run pages/Financial_Independence.py
   ```

## File Structure
```plaintext
├── pages
│   ├── Financial_Independence.py
│   ├── Investment_Advice_Tester.py
│   ├── Market_Research.py
│   └── Portfolio_Analysis.py
├── requirements.txt
└── README.md
```
