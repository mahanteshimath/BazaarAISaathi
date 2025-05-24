# Organized imports
import streamlit as st
from breeze_connect import BreezeConnect
import urllib
import pandas as pd
import requests
import json
import hashlib
from datetime import datetime, timezone

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
# if "historical_data" not in st.session_state:
#     st.session_state["historical_data"] = None

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


# Ensure unique labels or keys for all buttons
if st.button("Fetch Historical Data", key="fetch_historical_data_button_1"):
    try:
        # Initialize SDK
        api = BreezeConnect(api_key=api_key)

        # Generate Session
        api.generate_session(api_secret=api_secret, session_token=session_token)

        # Fetch Data using historical data API v2
        data = api.get_historical_data(
            interval=interval,
            from_date=from_date,
            to_date=to_date,
            stock_code=stock_code,
            exchange_code="NSE",
            product_type="cash"
        )
        st.write(data)
        # Convert data (API JSON response) into a table / dataframe using pandas library
        df = pd.DataFrame(data['Success'])

        # Display historical data in a dataframe
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

st.divider()

st.markdown("### Fetch Historical Data")


# Use Streamlit columns to organize input fields into two columns
col3, col4 = st.columns(2)

# Input fields for API credentials in the first column
with col3:
    interval = st.selectbox("Select Interval:",  ["minute", "5minute", "30minute", "day"], key="interval_fetch")
    # Updated input fields for date and time selection
    from_date_date = st.date_input("From Date:", key="from_date_date_fetch")
    from_date_time = st.time_input("From Time:", key="from_date_time_fetch")
    


# Input fields for session token and historical data parameters in the second column
with col4:
    to_date_date = st.date_input("To Date:", key="to_date_date_fetch")
    to_date_time = st.time_input("To Time:", key="to_date_time_fetch")
    stock_code = st.text_input("Stock Code:", "RELIND", key="historical_stock_code_fetch")
    


# Convert selected date and time to ISO 8601 format
from_date = f"{from_date_date}T{from_date_time}:00.000Z"
to_date = f"{to_date_date}T{to_date_time}:00.000Z"
st.write(f"From Date: {from_date}")
st.write(f"To Date: {to_date}")

st.markdown(f"""
breeze.get_historical_data(
    interval="{interval}",
    from_date="{from_date}",
    to_date="{to_date}",
    stock_code="{stock_code}",
    exchange_code="NSE",
    product_type="cash"
)

""")
if st.button("Fetch Historical Data"):
    try:
        # Define API details
        customerDetail_url = "https://api.icicidirect.com/breezeapi/api/v1/customerdetails"
        secret_key = api_secret
        appkey = api_key
        session_key = session_token
        time_stamp = datetime.now(timezone.utc).isoformat()[:19] + '.000Z'

        # Fetch session token
        customerDetail_payload = json.dumps({
            "SessionToken": session_key,
            "AppKey": appkey
        })

        customerDetail_headers = {
            'Content-Type': 'application/json',
        }

        customerDetail_response = requests.request("GET", customerDetail_url, headers=customerDetail_headers, data=customerDetail_payload)
        data = json.loads(customerDetail_response.text)

        # Log the raw API response for debugging
        st.write("Raw API Response:", json.dumps(data, indent=4))

        # Validate API response before accessing nested fields
        if data and "Success" in data and data["Success"]:
            session_token = data["Success"].get("session_token")
            if not session_token:
                st.error("Error: 'session_token' is missing in the API response.")
                st.stop()
        else:
            error_message = data.get("Error", "Unknown error") if isinstance(data, dict) else "Invalid response format"
            st.error(f"Error: Invalid API response structure or 'Success' field is missing. Details: {error_message}")
            st.stop()

        # Define historical data API details
        url = "https://api.icicidirect.com/breezeapi/api/v1/historicalcharts"
        
        # Ensure proper formatting of payload and timestamp for checksum generation
        payload = json.dumps({
            "interval": interval,
            "from_date": from_date,
            "to_date": to_date,
            "stock_code": stock_code,
            "exchange_code": "NSE",
            "product_type": "Cash"
        }, separators=(',', ':'))  # Compact JSON format

        # Generate checksum with correct concatenation order
        checksum_string = time_stamp + payload + secret_key
        checksum = hashlib.sha256(checksum_string.encode("utf-8")).hexdigest()

        headers = {
            'Content-Type': 'application/json',
            'X-Checksum': 'token ' + checksum,
            'X-Timestamp': time_stamp,
            'X-AppKey': appkey,
            'X-SessionToken': session_token
        }

        # Validate the interval parameter
        valid_intervals = ["minute", "5minute", "30minute", "day"]
        if interval not in valid_intervals:
            st.error(f"Invalid interval: {interval}. Please select one of {valid_intervals}.")
            st.stop()

        # Fetch historical data
        response = requests.request("GET", url, headers=headers, data=payload)
        historical_data = json.loads(response.text)

        # Log the raw API response for debugging
        st.write("Raw API Response:", json.dumps(historical_data, indent=4))

        # Validate and process historical data
        if 'Success' in historical_data and isinstance(historical_data['Success'], list):
            df = pd.DataFrame(historical_data['Success'])

            # Check if 'datetime' field exists and is valid
            if 'datetime' in df.columns:
                try:
                    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
                    df = df.dropna(subset=['datetime'])  # Drop rows with invalid datetime
                    df.set_index('datetime', inplace=True)

                    # Display historical data in a dataframe
                    st.markdown("### Historical Data")
                    st.dataframe(df)

                    # Display historical data in a chart
                    st.markdown("### Historical Data Chart")
                    st.line_chart(df[['open', 'high', 'low', 'close']])
                except Exception as e:
                    st.error(f"Error processing 'datetime' field: {e}")
            else:
                st.error("Error: 'datetime' field is missing in the API response.")
        else:
            error_message = historical_data.get("Error", "Unknown error") if isinstance(historical_data, dict) else "Invalid response format"
            st.error(f"Error: Invalid API response structure. Details: {error_message}")

    except Exception as e:
        st.error(f"Error fetching historical data: {e}")

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