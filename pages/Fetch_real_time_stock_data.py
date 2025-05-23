# Organized imports
import streamlit as st
from breeze_connect import BreezeConnect
import urllib
import pandas as pd

# Title and description
st.title("Fetch Real-Time Stock Data")
st.write("This allows you to fetch real-time stock data using the ICICI Direct API. Please enter your API credentials to get started.")

# Use Streamlit columns to organize input fields into two columns
col1, col2 = st.columns(2)

# Input fields for API credentials in the first column
with col1:
    api_key = st.text_input("Enter API Key:", type="password")
    api_secret = st.text_input("Enter API Secret:", type="password")

# Input fields for session token and historical data parameters in the second column
with col2:
    session_token = st.text_input("Enter Session Token:", type="password")
    from_date = st.text_input("From Date (YYYY-MM-DDTHH:MM:SS.000Z):", "2025-02-03T09:20:00.000Z")
    to_date = st.text_input("To Date (YYYY-MM-DDTHH:MM:SS.000Z):", "2025-02-03T09:22:00.000Z")
    stock_code = st.text_input("Stock Code:", "RELIND")

# Initialize SDK only if API Key is provided
if api_key:
    breeze = BreezeConnect(api_key=api_key)
else:
    breeze = None

# Display session key URL
st.write("Obtain your session key from the following URL:")
st.code("https://api.icicidirect.com/apiuser/login?api_key=" + urllib.parse.quote_plus("your_api_key"))

# Cache session and fetched data
if "session_cached" not in st.session_state:
    st.session_state["session_cached"] = None
if "customer_details" not in st.session_state:
    st.session_state["customer_details"] = None
if "historical_data" not in st.session_state:
    st.session_state["historical_data"] = None

# Function to connect and fetch data
def connect_and_fetch():
    try:
        # Generate session and cache it
        breeze.generate_session(api_secret=api_secret, session_token=session_token)
        st.session_state["session_cached"] = True
        st.success("Connected successfully!")

        # Fetch customer details
        st.session_state["customer_details"] = breeze.get_customer_details(api_session=session_token)

        # # Fetch historical data
        # st.session_state["historical_data"] = breeze.get_historical_data(
        #     interval="1minute",
        #     from_date="2025-02-03T09:20:00.000Z",
        #     to_date="2025-02-03T09:22:00.000Z",
        #     stock_code="RELIND",
        #     exchange_code="NSE",
        #     product_type="cash"
        # )

        # Connect to WebSocket
        breeze.ws_connect()
        st.success("WebSocket connected successfully!")
    except Exception as e:
        st.error(f"Error connecting: {e}")

# Function to disconnect WebSocket
def disconnect():
    breeze.ws_disconnect()
    st.write("Disconnected from WebSocket.")

# Function to display customer details
def display_customer_details():
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

# Updated the fetch_and_display_historical_data function to handle cases where historical data is None
def fetch_and_display_historical_data(from_date, to_date, stock_code):
    try:
        # Fetch historical data
        st.session_state["historical_data"] = breeze.get_historical_data(
            interval="1minute",
            from_date=from_date,
            to_date=to_date,
            stock_code=stock_code,
            exchange_code="NSE",
            product_type="cash"
        )

        # Check if historical data is None
        if not st.session_state["historical_data"] or "Success" not in st.session_state["historical_data"]:
            st.error("No historical data found for the given parameters.")
            return

        # Display historical data in a dataframe
        historical_data = st.session_state["historical_data"]['Success']
        df = pd.DataFrame(historical_data)
        st.markdown("### Historical Data")
        st.dataframe(df)

        # Display historical data in a chart
        st.markdown("### Historical Data Chart")
        df['datetime'] = pd.to_datetime(df['datetime'])
        df.set_index('datetime', inplace=True)
        st.line_chart(df[['open', 'high', 'low', 'close']])
    except Exception as e:
        st.error(f"Error fetching historical data: {e}")

# Buttons to trigger actions
if st.button("Connect"):
    connect_and_fetch()

if st.button("Disconnect WebSocket"):
    disconnect()

# Display data
if st.session_state["customer_details"]:
    display_customer_details()


st.markdown("### Fetch Historical Data")
if st.button("Fetch Historical Data"):
    fetch_and_display_historical_data(from_date, to_date, stock_code)
    
# Footer
footer = """<style>
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
st.markdown(footer, unsafe_allow_html=True)