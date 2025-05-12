import streamlit as st
import requests
import json
from utils.get_market_insights import get_market_insights, get_top_gainers_and_losers

st.title("Today's Market Indicators")
st.write(
    """
    This page provides a comprehensive overview of various market indicators that can be used to analyze and predict stock market trends. 
    The indicators are categorized into different sections for better understanding and usability.
    """
)

def fetch_market_insights():
    api_key = st.secrets["PERPLEXITY_API_KEY"]
    return get_market_insights(api_key)

if st.button("Get Latest Market Insights"):
    with st.spinner("Fetching market insights..."):
        insights = fetch_market_insights()

        if "error" in insights:
            st.error(f"Error fetching insights: {insights['error']}")
        elif "content" in insights:
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

        def fetch_top_gainers_and_losers():
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            return get_top_gainers_and_losers(api_key)

        st.write("-----")
        st.subheader("Top 5 Gainers and Losers")

        # Fetch and display top gainers and losers
        gainers_and_losers = fetch_top_gainers_and_losers()
        if "error" in gainers_and_losers:
            st.error(f"Error fetching data: {gainers_and_losers['error']}")
        elif "content" in gainers_and_losers:
            st.write(gainers_and_losers["content"])

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