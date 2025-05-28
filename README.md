# BazaarAISaathi
Your AI Friend in the Stock Market 🤖📈

![App Architecture](src/App_Architecture.jpg)

## Overview
BazaarAISaathi is an AI-powered platform designed to empower investors with actionable insights into the Indian stock market. Leveraging advanced natural language processing, real-time data analytics, and expert-driven financial modeling, the app delivers personalized investment strategies, market sentiment analysis, and portfolio optimization recommendations.

## 🚀 Key Features
- 🧮 **Financial Independence Planner (FIRE):** Create detailed, personalized plans for financial independence using inputs like age, salary, marital status, and more.
- 📝 **Investment Advice Tester:** Submit investment tips via text or image. The app extracts text (using EasyOCR) and provides AI-driven analysis and validation.
- 📊 **Fundamental & Technical Analysis:** Access comprehensive reports on company fundamentals, technical indicators, market sentiment, and trading strategies.
- 📈 **Portfolio Analysis:** Upload or paste your portfolio for in-depth, multi-dimensional analysis and stock-wise recommendations.
- 🔍 **Market Research & Competitor Benchmarking:** Use AI-driven research to assess industry trends, compare competitors, and identify new opportunities.
- 📉 **Deep Market Insights:** Stay updated with real-time indicators such as top gainers/losers, macroeconomic trends, and critical market data.
- ⏱️ **Real-Time Stock Data:** Fetch and analyze live stock prices and trends for informed decision-making.
- 🧪 **Hypothesis Testing:** Test investment hypotheses using historical and real-time data.
- 💭 **Ask Finance Questions:** Get expert answers to any finance-related queries using advanced AI technology.
- 📚 **Investment Books Summary:** Access concise summaries of top 50 investment books for quick learning and reference.


## 🛠️ Technologies Used
- **Streamlit:** Interactive web app framework.
- **Perplexity AI & LangChain:** Advanced NLP and financial forecasting.
- **Pandas, Plotly, BeautifulSoup:** Data manipulation and visualization.
- **EasyOCR & Docling Parse:** Text extraction from images and PDFs.
- **Python Ecosystem:** Including requests, python-dotenv, and more.

## ⚡ Installation & Setup
1. **Clone the Repository:**
   ```powershell
   git clone https://github.com/yourusername/BazaarAISaathi.git
   cd BazaarAISaathi
   ```
2. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Configure API Keys:**
   - Set up your Streamlit secrets and API keys (Perplexity, etc.) in a `secrets.toml` file.
4. **Run the App:**
   ```powershell
   streamlit run Home.py
   ```
   - Or run any specific module from the `pages/` directory, e.g.:
   ```powershell
   streamlit run pages/Financial_Independence.py
   ```

## 📁 File Structure
```plaintext
├── Home.py
├── README.md
├── requirements.txt
├── pages
│   ├── Architecture.py
│   ├── Deep_Research.py
│   ├── Fetch_real_time_stock_data.py
│   ├── Finance_with_Perplexity.py
│   ├── Financial_Independence.py
│   ├── Hypothesis.py
│   ├── Market_Indicators.py
│   ├── Portfolio_Analysis.py
│   ├── Stocks_List.py
│   ├── Techno_Fund_Analysis.py
│   └── Tip_Tester.py
├── src
│   ├── Architecture_app.txt
│   ├── BSE_Equity.csv
│   ├── holdings.csv
│   ├── India.jpeg
│   ├── NSE_EQUITYS.csv
│   └── Top50Books.csv
├── utils
│   ├── deep_research.py
│   ├── finance_utils.py
│   ├── fire_planner.py
│   ├── get_market_insights.py
│   ├── portfolio_analysis.py
│   ├── RealTime_stock_price_analysis.py
│   └── tip_analysis.py
```

## 🤝 Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements and new features.

## 📄 License
[MIT License](LICENSE)

## 📬 Contact
For questions or support, please open an issue or contact the maintainer at <mahanteshimath@gmail.com>.
