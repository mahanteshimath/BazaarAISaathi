# Import necessary standard libraries
import asyncio  # For running asynchronous code
import os       # To access environment variables
import requests  # For making API requests
import json  # For handling JSON responses
import streamlit as st

# Retrieve configuration from environment variables or use defaults
BASE_URL = os.getenv("EXAMPLE_BASE_URL", "https://api.perplexity.ai")
API_KEY = st.secrets["PERPLEXITY_API_KEY"]

MODEL_NAME = os.getenv("EXAMPLE_MODEL_NAME", "sonar-pro")

# Validate that all required configuration variables are set
if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError(
        "Please set EXAMPLE_BASE_URL, EXAMPLE_API_KEY, EXAMPLE_MODEL_NAME via env var or code."
    )
class FinanceDocumentSummarizer:
    """A class to summarize finance documents using the Perplexity API."""

    def summarize_with_api(self, document_link, api_key):
        """Summarize the given document link using the Perplexity API.

        Args:
            document_link (str): The public link to the document to summarize.
            api_key (str): The API key for authentication.

        Returns:
            dict: A dictionary containing the summarized content or an error message.
        """
        api_endpoint = f"{BASE_URL}/chat/completions"

        payload = {
            "model": MODEL_NAME,
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

# Import nest_asyncio to support nested event loops (helpful in interactive environments like Jupyter)
import nest_asyncio

# Apply the nest_asyncio patch to enable running asyncio.run() even if an event loop is already running.
nest_asyncio.apply()

async def main():
    """
    Main asynchronous function to set up and run the agent.

    This function creates an Agent with a custom model and function tools,
    then runs a query to summarize a document.
    """
    document_link = "https://example.com/document.pdf"
    summarizer = FinanceDocumentSummarizer()
    result = summarizer.summarize_with_api(document_link, API_KEY)

    # Print the final output from the agent.
    print(result)

# Standard boilerplate to run the async main() function.
if __name__ == "__main__":
    asyncio.run(main())
