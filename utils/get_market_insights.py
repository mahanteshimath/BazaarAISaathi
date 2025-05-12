import requests
import json

def get_market_insights(api_key):
    api_endpoint = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise. Focus on key market indicators and their current values."
            },
            {
                "role": "user",
                "content": "List all Indicators which will help to understand today's Indian Market and also provide the latest news related to these indicators."
            }
        ]
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
            citations = []

            # Find citations from the result
            if isinstance(result, dict):
                citations = result.get('citations', [])
                if not citations and 'choices' in result:
                    for choice in result['choices']:
                        if isinstance(choice, dict) and 'message' in choice:
                            citations.extend(choice['message'].get('citations', []))

            return {
                "content": content,
                "citations": citations
            }
        return result
    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse response: {str(e)}"}

def get_top_gainers_and_losers(api_key):
    api_endpoint = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise. Focus on the top 5 gainers and losers in today's Indian stock market."
            },
            {
                "role": "user",
                "content": "List the top 5 gainers and losers in today's Indian stock market along with their percentage changes."
            }
        ]
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
            citations = []

            # Find citations from the result
            if isinstance(result, dict):
                citations = result.get('citations', [])
                if not citations and 'choices' in result:
                    for choice in result['choices']:
                        if isinstance(choice, dict) and 'message' in choice:
                            citations.extend(choice['message'].get('citations', []))

            return {
                "content": content,
                "citations": citations
            }
        return result
    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse response: {str(e)}"}
