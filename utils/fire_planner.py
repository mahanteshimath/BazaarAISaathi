import requests
import json

def generate_fire_plan(salary, years, essentials, non_essentials, savings_pct, investment_types, side_income, skills, api_key):
    """
    Generate a FIRE plan using the provided user inputs and an external API.
    """
    api_endpoint = "https://api.perplexity.ai/chat/completions"
    prompt = f"""
    Create a detailed plan for achieving financial independence within a {years}-year timeframe on a salary of {salary} rupees per month.\n
    The plan should include:\n- Specific savings goals (Essentials: {essentials}, Non-essentials: {non_essentials}, Savings %: {savings_pct})\n- Investment strategies (Types: {investment_types})\n- Potential side income sources (e.g., {side_income})\n- A clear breakdown of monthly expenses\n- Recommended savings percentage\n- Types of investments to consider\n- Skills to develop to increase earning potential: {skills}\n\nConsider inflation and cost of living increases during the next {years} years.\nProvide a clear, actionable, step-by-step plan.\n
    
        
    The plan should include specific savings goals, investment strategies, and potential side income sources. Provide a clear breakdown of monthly expenses, recommended savings percentage, and types of investments to consider, such as stocks, mutual funds, or real estate. Additionally, outline any skills that could be developed to increase earning potential over this period. 

    ### Steps
    1. **Analyze Monthly Budget**: Break down expenses into essential and non-essential categories. Set a realistic savings target.
    2. **Determine Savings Rate**: Decide on a percentage of income to save each month. Aim for at least 20-30% of monthly salary.
    3. **Investment Strategy**: Research and select suitable investment vehicles, considering risk tolerance.
    4. **Side Income Opportunities**: Identify potential skills or hobbies that could be monetized. Explore freelance work, part-time jobs, or small businesses.
    5. **Skill Development**: List key skills to acquire that would lead to promotions or higher-paying job opportunities.
    6. **Review and Adjust**: Set regular intervals (e.g., every 6 months) to review financial progress and adjust the plan as necessary.

    ### Output Format
    - A detailed written plan consisting of:
    - Monthly budget outline,
    - Yearly savings goals,
    - A diversified investment portfolio (with examples),
    - List of potential side income sources,
    - Skill acquisition roadmap.

    ### Examples
    - **Budget Breakdown**: "Monthly salary = 50,000 rupees\n   Essentials = 25,000\n   Non-essentials = 10,000\n   Savings = 15,000\n"
    - **Investment Portfolio**: "Suggested investment: 60% in mutual funds, 20% in stocks, and 20% in savings accounts or bonds."
    - **Side Income**: "Freelancing as a graphic designer or tutoring in mathematics."

    ### Notes
    - Consider inflation and cost of living increases during the next 10 years when planning.
    - Invest in continuous education to adapt to market changes.
    
    
    """
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
