import pandas as pd
import requests
import json

def get_top_10_learnings(book_name, api_key):
    api_endpoint = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": "Summarize the top 10 learnings from the book provided."
            },
            {
                "role": "user",
                "content": f"Summarize the top 10 learnings from the book '{book_name}'."
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
            return content
        return result
    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse response: {str(e)}"}
def ask_finance_question(question, api_key):
    api_endpoint = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar-pro",
        "messages": [
            {
                "role": "system",
                "content": "Answer the question as a finance expert. Include relevant citations and sources for the information provided."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "web_search_options": {
            "user_location": {
                "country": "IN"
            }
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

            # Format content as Markdown
            markdown_response = f"### Answer\n\n{content}\n\n"
            if citations:
                markdown_response += "\n### Sources\n"
                for citation in citations:
                    markdown_response += f"- {citation}\n"

            return markdown_response
        return result
    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse response: {str(e)}"}

def load_books(file_path):
    try:
        books_df = pd.read_csv(file_path, encoding='utf-8')
        return books_df
    except Exception as e:
        return {"error": f"Failed to load books: {str(e)}"}
