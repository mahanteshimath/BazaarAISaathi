import requests
import json

def perform_market_analysis(prompt, api_key):
    api_endpoint = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": "Perform a detailed market analysis based on the provided prompt."
            },
            {
                "role": "user",
                "content": prompt
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
            citations = result.get('citations', [])

            return {
                'content': content,
                'citations': citations
            }
        return result
    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse response: {str(e)}"}
