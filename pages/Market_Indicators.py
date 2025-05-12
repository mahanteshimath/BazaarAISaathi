import streamlit as st
import requests
import json

st.title("Today's Market Indicators")
st.write(
    """
    This page provides a comprehensive overview of various market indicators that can be used to analyze and predict stock market trends. 
    The indicators are categorized into different sections for better understanding and usability.
    """
)

def get_market_insights():
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
        api_key = st.secrets["PERPLEXITY_API_KEY"]
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
    except KeyError as e:
        return {"error": f"Missing key in secrets: {str(e)}"}

if st.button("Get Latest Market Insights"):
    with st.spinner("Fetching market insights..."):
        insights = get_market_insights()
        
        if "error" in insights:
            st.error(f"Error fetching insights: {insights['error']}")
        elif "content" in insights:
            st.subheader("Market Analysis")
            st.write(insights["content"])
            
            if insights["citations"]:
                st.subheader("Sources")
                for i, citation in enumerate(insights["citations"]):
                    if isinstance(citation, dict):
                        title = citation.get('title', 'Source')
                        url = citation.get('url', '#')
                    else:
                        title = 'Source'
                        url = citation if isinstance(citation, str) else '#'
                    st.markdown(f"{i+1}. [{title}]({url})")
        else:
            st.json(insights)

st.write("-----")
st.subheader("Top 5 Gainers and Losers")
st.write(
    """
    Here are the top 5 gainers and losers in today's market:
    """
)



st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: blue;
        color: white; # Adjust this for expander header color
    }
    .streamlit-expanderContent {
        background-color: blue;
        color: white; # Expander content color
    }
    </style>
    ''',
    unsafe_allow_html=True
)

footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #2C1E5B;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/mahantesh-hiremath/" target="_blank">MAHANTESH HIREMATH</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)