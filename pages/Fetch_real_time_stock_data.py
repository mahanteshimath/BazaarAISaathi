import streamlit as st
from breeze_connect import BreezeConnect
import urllib
import numpy as np

# Initialize SDK
breeze = BreezeConnect(api_key="your_api_key")

# Obtain your session key from the URL
st.write("Obtain your session key from the following URL:")
st.code("https://api.icicidirect.com/apiuser/login?api_key=" + urllib.parse.quote_plus("your_api_key"))

# Input fields for API secret and session token
api_secret = st.text_input("Enter API Secret:", type="password")
session_token = st.text_input("Enter Session Token:", type="password")

# Add a button to connect
if st.button("Connect"):
    try:
        breeze.generate_session(api_secret=api_secret, session_token=session_token)
        st.success("Connected successfully!")
    except Exception as e:
        st.error(f"Error connecting: {e}")

# Connect to WebSocket (it will connect to tick-by-tick data server)
breeze.ws_connect()

# Callback to receive ticks
def on_ticks(ticks):
    st.write("Ticks: {}".format(ticks))

# Assign the callbacks
breeze.on_ticks = on_ticks

# Disconnect WebSocket (it will disconnect from all actively connected servers)
def disconnect():
    breeze.ws_disconnect()
    st.write("Disconnected from WebSocket.")

# Add a button to disconnect
if st.button("Disconnect WebSocket"):
    disconnect()

# Fetch historical data
def fetch_historical_data():
    try:
        historical_data = breeze.get_historical_data(
            interval="1minute",
            from_date="2025-02-03T09:20:00.000Z",
            to_date="2025-02-03T09:22:00.000Z",
            stock_code="RELIND",
            exchange_code="NSE",
            product_type="cash"
        )
        st.write("Historical Data:")
        st.json(historical_data)
    except Exception as e:
        st.error(f"Error fetching historical data: {e}")

# Add a button to fetch historical data
if st.button("Fetch Historical Data"):
    fetch_historical_data()

# Fetch customer details
def fetch_customer_details():
    try:
        customer_details = breeze.get_customer_details(api_session="your_api_session")
        st.write("Customer Details:")
        st.json(customer_details)
    except Exception as e:
        st.error(f"Error fetching customer details: {e}")

# Add a button to fetch customer details
if st.button("Fetch Customer Details"):
    fetch_customer_details()

st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: blue;
        color: white; /* Adjust this for expander header color */
    }
    .streamlit-expanderContent {
        background-color: blue;
        color: white; /* Expander content color */
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
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/mahantesh-hiremath/ " target="_blank">MAHANTESH HIREMATH</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)