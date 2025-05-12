import streamlit as st
import pandas as pd

# Load NSE_EQUITYS.csv file
file_path = "./src/NSE_EQUITYS.csv"
try:
    nse_data = pd.read_csv(file_path)
    company_names = nse_data["NAME OF COMPANY"].tolist()

    st.title("Fundamental Analysis")
    st.write("### Select a Company")

    selected_company = st.selectbox("Choose a company for analysis:", company_names)

    if selected_company:
        company_info = nse_data[nse_data["NAME OF COMPANY"] == selected_company].iloc[0]
        symbol = company_info["SYMBOL"]
        Listed_Name=f"{symbol}:{selected_company}"
        st.write(f"**Selected Company:** {Listed_Name}")

except Exception as e:
    st.error(f"Failed to load NSE data: {str(e)}")

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