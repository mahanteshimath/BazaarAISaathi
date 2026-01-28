import requests
import json

def analyze_tip_or_advice(tip_text, api_key):
    """
    Analyze the given investment tip or advice using an external API.

    Args:
        tip_text (str): The investment tip or advice to analyze.
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
                "content": "Act as an Experienced sucessful/profitable Indian stock market investor. Do Not add any disclaimer that I am not SEBI registered investment advisor or AI generated content. Analyze the following investment tip or advice. Provide a detailed analysis including potential risks, opportunities, and overall feasibility."
            },
            {
                "role": "user",
                "content": tip_text
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
