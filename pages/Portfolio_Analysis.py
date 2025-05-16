import streamlit as st
from utils.portfolio_analysis import analyze_portfolio, parse_portfolio_file, parse_portfolio_text
import pandas as pd

st.title("Portfolio Analysis")

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

st.header("Upload or Paste Your Portfolio")

portfolio_text = st.text_area("Paste your portfolio data (CSV or tabular format)", height=120, placeholder="INSTRUMENT\tQTY.\tAVG. COST\tLTP\tINVESTED\tCUR. VAL\tP&L\nASIANPAINT\t15\t2586.67\t2353.15\t38800\t35297.25\t-3502.75\n...")
uploaded_file = st.file_uploader("Or upload your portfolio file (CSV or Excel)", type=["csv", "xls", "xlsx"])

portfolio_df = None
if uploaded_file:
    try:
        portfolio_df = parse_portfolio_file(uploaded_file)
        st.success("Portfolio file loaded successfully.")
    except Exception as e:
        st.error(f"Failed to parse file: {e}")
elif portfolio_text:
    try:
        portfolio_df = parse_portfolio_text(portfolio_text)
        st.success("Portfolio text parsed successfully.")
    except Exception as e:
        st.error(f"Failed to parse text: {e}")

if portfolio_df is not None:
    st.subheader("Portfolio Preview")
    st.dataframe(portfolio_df)
    if st.button("Run Portfolio Analysis", key="run_portfolio_analysis"):
        with st.spinner("Analyzing your portfolio..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            results = analyze_portfolio(portfolio_df, api_key)
            st.subheader("Stock-wise Recommendations")
            for res in results:
                st.markdown(f"**{res['stock']}**: {res['analysis']}")

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
st.markdown(footer,unsafe_allow_html=True)