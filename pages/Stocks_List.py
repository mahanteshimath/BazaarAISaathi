import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import io

st.title("All listed Stocks in India")
st.write("This page displays all the stocks listed on the Indian stock exchanges.")

# ---------------------- Step 1: Fetch NSE Companies ---------------------- #
@st.cache_data
def fetch_nse():
    url = "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv"
    headers = {'User-Agent': 'Mozilla/5.0'}
    s = requests.Session()
    s.headers.update(headers)
    r = s.get(url)
    df_nse = pd.read_csv(io.BytesIO(r.content))
    df_nse['Exchange'] = 'NSE'
    return df_nse[['SYMBOL', 'NAME OF COMPANY', 'Exchange']]

# ---------------------- Step 2: Fetch BSE Companies ---------------------- #
@st.cache_data
def fetch_bse():
    url = "https://www.bseindia.com/corporates/List_Scrips.aspx"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the download link or fallback to parsing table if available
    try:
        csv_link = "https://www.bseindia.com/download/BhavCopy/Equity/EQ250423_CSV.ZIP"
        # This above URL is placeholder; BSE doesn't provide easy company list via static link.
        # Instead, scrape the HTML table
        tables = pd.read_html(response.text)
        for table in tables:
            if 'Security Code' in table.columns or 'Security Id' in table.columns:
                df_bse = table.copy()
                break
        else:
            st.warning("BSE company table not found.")
            return pd.DataFrame()

        # Clean and standardize
        df_bse = df_bse.rename(columns={
            "Security Id": "SYMBOL",
            "Security Name": "NAME OF COMPANY"
        })
        df_bse['Exchange'] = 'BSE'
        return df_bse[['SYMBOL', 'NAME OF COMPANY', 'Exchange']]

    except Exception as e:
        st.error(f"Error fetching BSE data: {e}")
        return pd.DataFrame()

# ---------------------- Step 3: Merge and Show ---------------------- #
st.info("Fetching data from NSE and BSE...")

nse_df = fetch_nse()
bse_df = fetch_bse()

if not nse_df.empty and not bse_df.empty:
    merged_df = pd.merge(nse_df, bse_df, on='SYMBOL', how='outer', suffixes=('_NSE', '_BSE'))

    st.success(f"✅ Fetched {len(nse_df)} from NSE and {len(bse_df)} from BSE. Merged total: {len(merged_df)} companies.")
    st.dataframe(merged_df.head(50))

    csv = merged_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Full CSV", data=csv, file_name="merged_nse_bse_companies.csv", mime='text/csv')
else:
    st.warning("Data not available from one or both sources.")

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