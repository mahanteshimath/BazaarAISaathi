import requests
import json
import pandas as pd
from io import StringIO

def analyze_portfolio(df, api_key):
    """
    Analyze each stock in the portfolio and provide a recommendation (BUY, SELL, HOLD) with reasoning and price targets.
    """
    api_endpoint = "https://api.perplexity.ai/chat/completions"
    results = []
    for _, row in df.iterrows():
        stock_info = f"INSTRUMENT: {row['INSTRUMENT']}, QTY: {row['QTY.']}, AVG. COST: {row['AVG. COST']}, LTP: {row['LTP']}, INVESTED: {row['INVESTED']}, CUR. VAL: {row['CUR. VAL']}, P&L: {row['P&L']}"
        prompt = f"""
        Act as an Experienced sucessful/profitable Indian stock market invester. Do Not add any declaimer that I am not SEBI registered investment advicer or AI generated content. Analyze the following stock from a portfolio and provide a clear recommendation (BUY, SELL, or HOLD).\n
        Stock details: {stock_info}\n
        For BUY: Suggest a price range to accumulate.\n        For SELL: Suggest a target price and reason.\n        For HOLD: Give a reason for holding.\n        Use fundamental and technical reasoning.\n        """
        payload = {
            "model": "sonar-pro",
            "messages": [
                {"role": "system", "content": "You are a stock market analysis expert."},
                {"role": "user", "content": prompt}
            ],
        "web_search_options": {
            "user_location": {"country": "IN"}
        }
        }
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            response = requests.post(api_endpoint, json=payload, headers=headers, timeout=30)
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                message = result['choices'][0]['message']
                content = message.get('content', '')
                results.append({"stock": row['INSTRUMENT'], "analysis": content})
            else:
                results.append({"stock": row['INSTRUMENT'], "analysis": "No analysis available."})
        except Exception as e:
            results.append({"stock": row['INSTRUMENT'], "analysis": f"Error: {str(e)}"})
    return results

def parse_portfolio_file(uploaded_file):
    """
    Parse uploaded CSV or Excel file into a DataFrame.
    """
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")
    return df

def parse_portfolio_text(text):
    """
    Parse pasted text into a DataFrame.
    """
    df = pd.read_csv(StringIO(text), sep='\t|,', engine='python')
    return df
