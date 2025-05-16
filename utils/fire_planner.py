import requests
import json

def generate_fire_plan(salary, years, essentials, non_essentials, savings_pct, investment_types, side_income, skills, api_key):
    """
    Generate a FIRE plan using the provided user inputs and an external API.
    """
    api_endpoint = "https://api.perplexity.ai/chat/completions"
    prompt = f"""
    Create a detailed plan for achieving financial independence within a {years}-year timeframe on a salary of {salary} rupees per month.\n
    The plan should include:\n- Specific savings goals (Essentials: {essentials}, Non-essentials: {non_essentials}, Savings %: {savings_pct})\n- Investment strategies (Types: {investment_types})\n- Potential side income sources (e.g., {side_income})\n- A clear breakdown of monthly expenses\n- Recommended savings percentage\n- Types of investments to consider\n- Skills to develop to increase earning potential: {skills}\n\nConsider inflation and cost of living increases during the next {years} years.\nProvide a clear, actionable, step-by-step plan.\n"""
    payload = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are a financial planning expert."},
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
