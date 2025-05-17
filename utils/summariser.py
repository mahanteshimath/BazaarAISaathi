import requests
import json

class FinanceDocumentSummarizer:
    """A class to summarize finance documents using an external API."""

    def summarize_with_api(self, document_link, api_key):
        """Summarize the given document link using an external API.

        Args:
            document_link (str): The public link to the document to summarize.
            api_key (str): The API key for authentication.

        Returns:
            dict: A dictionary containing the summarized content or an error message.
        """
        api_endpoint = "https://api.perplexity.ai/chat/completions"

        payload = {
            "model": "sonar-reasoning-pro",
            "messages": [
                {
                    "role": "system",
                    "content": "Summarize the content of the document available at the provided link."
                },
                {
                    "role": "user",
                    "content": document_link
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
