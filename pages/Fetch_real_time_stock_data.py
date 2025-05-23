import streamlit as st
from breeze_connect import BreezeConnect
import urllib
import numpy as np

# Input fields for API key, API secret, and session token
api_key = st.text_input("Enter API Key:", type="password")
api_secret = st.text_input("Enter API Secret:", type="password")
session_token = st.text_input("Enter Session Token:", type="password")

# Initialize SDK
breeze = BreezeConnect(api_key=api_key)

# Obtain your session key from the URL
st.write("Obtain your session key from the following URL:")
st.code("https://api.icicidirect.com/apiuser/login?api_key=" + urllib.parse.quote_plus("your_api_key"))



# Cache session and fetched data
if "session_cached" not in st.session_state:
    st.session_state["session_cached"] = None
if "customer_details" not in st.session_state:
    st.session_state["customer_details"] = None
if "historical_data" not in st.session_state:
    st.session_state["historical_data"] = None

# Add a title to the page
st.title("Fetch Real-Time Stock Data")

# Add a button to connect
if st.button("Connect"):
    try:
        # Generate session and cache it
        breeze.generate_session(api_secret=api_secret, session_token=session_token)
        st.session_state["session_cached"] = True
        st.success("Connected successfully!")

        # Fetch customer details
        customer_details = breeze.get_customer_details(api_session=session_token)
        st.session_state["customer_details"] = customer_details
        st.markdown("### Customer Details")
        st.json(customer_details)

        # Fetch historical data
        historical_data = breeze.get_historical_data(
            interval="1minute",
            from_date="2025-02-03T09:20:00.000Z",
            to_date="2025-02-03T09:22:00.000Z",
            stock_code="RELIND",
            exchange_code="NSE",
            product_type="cash"
        )
        st.session_state["historical_data"] = historical_data
        st.markdown("### Historical Data")
        st.json(historical_data)

        # Connect to WebSocket
        breeze.ws_connect()
        st.success("WebSocket connected successfully!")
    except Exception as e:
        st.error(f"Error connecting: {e}")

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

# Update the display of customer details
if st.session_state["customer_details"]:
    customer_details = st.session_state["customer_details"]
    st.markdown("### Customer Details")
    st.markdown("""
    - **User ID**: {idirect_userid}
    - **User Name**: {idirect_user_name}
    - **Last Login Time**: {idirect_lastlogin_time}
    - **Exchange Trade Dates**:
        - NSE: {nse_date}
        - BSE: {bse_date}
        - FNO: {fno_date}
        - NDX: {ndx_date}
    - **Exchange Status**:
        - NSE: {nse_status}
        - BSE: {bse_status}
        - FNO: {fno_status}
        - NDX: {ndx_status}
    - **Segments Allowed**:
        - Trading: {trading}
        - Equity: {equity}
        - Derivatives: {derivatives}
        - Currency: {currency}
    """.format(
        idirect_userid=customer_details['Success']['idirect_userid'],
        idirect_user_name=customer_details['Success']['idirect_user_name'],
        idirect_lastlogin_time=customer_details['Success']['idirect_lastlogin_time'],
        nse_date=customer_details['Success']['exg_trade_date']['NSE'],
        bse_date=customer_details['Success']['exg_trade_date']['BSE'],
        fno_date=customer_details['Success']['exg_trade_date']['FNO'],
        ndx_date=customer_details['Success']['exg_trade_date']['NDX'],
        nse_status=customer_details['Success']['exg_status']['NSE'],
        bse_status=customer_details['Success']['exg_status']['BSE'],
        fno_status=customer_details['Success']['exg_status']['FNO'],
        ndx_status=customer_details['Success']['exg_status']['NDX'],
        trading=customer_details['Success']['segments_allowed']['Trading'],
        equity=customer_details['Success']['segments_allowed']['Equity'],
        derivatives=customer_details['Success']['segments_allowed']['Derivatives'],
        currency=customer_details['Success']['segments_allowed']['Currency']
    ))

# Update the display of historical data
if st.session_state["historical_data"]:
    historical_data = st.session_state["historical_data"]['Success']
    st.markdown("### Historical Data")
    st.markdown("| DateTime | Stock Code | Exchange Code | Open | High | Low | Close | Volume |")
    st.markdown("|----------|------------|---------------|------|------|-----|-------|--------|")
    for record in historical_data:
        st.markdown("| {datetime} | {stock_code} | {exchange_code} | {open} | {high} | {low} | {close} | {volume} |".format(
            datetime=record['datetime'],
            stock_code=record['stock_code'],
            exchange_code=record['exchange_code'],
            open=record['open'],
            high=record['high'],
            low=record['low'],
            close=record['close'],
            volume=record['volume']
        ))

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