import requests
import json

def generate_fire_plan(age, salary, years, essentials, non_essentials, savings_pct, investment_types, side_income, skills, api_key):
    """
    Generate a FIRE plan using the provided user inputs and an external API.
    """
    api_endpoint = "https://api.perplexity.ai/chat/completions"
    prompt = (
        f"Create a detailed plan for achieving financial independence within a {years}-year timeframe "
        f"for a {age}-year-old earning {salary} rupees per month. "
        f"The plan should include specific savings goals, investment strategies ({investment_types}), and potential side income sources ({side_income}). "
        f"Provide a clear breakdown of monthly expenses (essentials: {essentials}, non-essentials: {non_essentials}), "
        f"recommended savings percentage ({savings_pct}%), and types of investments to consider. "
        f"Additionally, outline any skills ({skills}) that could be developed to increase earning potential over this period. "
        f"Consider inflation and cost of living increases during the next {years} years."
    )
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": "You are a 30+ years financial planning expert, Helping use client to achive FIRE amount with detailed plan."},
            {"role": "user", "content": prompt}
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
            citations = result.get('citations', [])
            return {"content": content, "citations": citations}
        return result
    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse response: {str(e)}"}
