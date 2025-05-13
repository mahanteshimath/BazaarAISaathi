import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import io

st.title("All listed Stocks in India")
st.write("This page displays all the stocks listed on the Indian stock exchanges.")

st.write("-----")
# ---------------------- Step 1: Read NSE Companies from CSV ---------------------- #
@st.cache_data
def read_nse():
    try:
        df_nse = pd.read_csv("src/NSE_EQUITYS.csv")
        df_nse['Exchange'] = 'NSE'
        return df_nse  # Return all columns
    except Exception as e:
        st.error(f"Error reading NSE data: {e}")
        return pd.DataFrame()
# ---------------------- Step 2: Read BSE Companies from CSV ---------------------- #
@st.cache_data
def read_bse():
    try:
        df_bse = pd.read_csv("src/BSE_Equity.csv")
        df_bse['Exchange'] = 'BSE'
        return df_bse  # Return all columns
    except Exception as e:
        st.error(f"Error reading BSE data: {e}")
        return pd.DataFrame()

nse_df = read_nse()
bse_df = read_bse()

# NSE Section
st.header("NSE Listed Companies")
if not nse_df.empty:
    st.success(f"✅ Total NSE Companies: {len(nse_df)}")
    st.dataframe(nse_df, use_container_width=True)
    csv_nse = nse_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download NSE CSV", data=csv_nse, file_name="nse_companies.csv", mime='text/csv')
st.write("-----")
# BSE Section
st.header("BSE Listed Companies")
if not bse_df.empty:
    st.success(f"✅ Total BSE Companies: {len(bse_df)}")
    st.dataframe(bse_df, use_container_width=True)
    csv_bse = bse_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download BSE CSV", data=csv_bse, file_name="bse_companies.csv", mime='text/csv')
st.write("-----")
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
st.markdown(footer,unsafe_allow_html=True)