import requests
import json

def analyze_real_time_stock_data(stock_data, api_key):
    """
    Analyze the given real-time stock data using an external API.

    Args:
        stock_data (dict): The real-time stock data to analyze.
        api_key (str): The API key for the external API.

    Returns:
        dict: A dictionary containing the analysis result or an error message.
    """
    api_endpoint = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": "You are 50+ years experienced financial analyst. Analyse give historical stock price data and provide insights on the investment tip or advice provided by the user. Provide a detailed analysis including potential risks, market conditions, and any relevant historical data that supports your analysis. Conlude with BUY HOLD SELL at current price recommendation based on the analysis." 
            },
            {
                "role": "user",
                "content": stock_data
            }
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
            return {"content": content}

        return result
    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse response: {str(e)}"}
