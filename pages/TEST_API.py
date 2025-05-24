import requests
import json
import hashlib
from datetime import datetime, timezone

customerDetail_url = "https://api.icicidirect.com/breezeapi/api/v1/customerdetails"
secret_key = "4%Y01K1m540*c42399j)33Y6Wh0C3728"
appkey = "#5552D0L5OB900l4P50Y64699F1w809o"
session_key = "51606286"
time_stamp = datetime.now(timezone.utc).isoformat()[:19] + '.000Z'

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
print("Raw API Response:", json.dumps(data, indent=4))

# Validate API response before accessing nested fields
if data and "Success" in data and data["Success"]:
    session_token = data["Success"].get("session_token")
    if not session_token:
        raise ValueError("Error: 'session_token' is missing in the API response.")
else:
    error_message = data.get("Error", "Unknown error") if isinstance(data, dict) else "Invalid response format"
    raise ValueError(f"Error: Invalid API response structure or 'Success' field is missing. Details: {error_message}")

url = "https://api.icicidirect.com/breezeapi/api/v1/historicalcharts"
payload = json.dumps({
    "interval": "5minute",
    "from_date": "2025-02-03T09:30:00.000Z",
    "to_date": "2025-02-03T10:15:00.000Z",
    "stock_code": "ITC",
    "exchange_code": "NSE",
    "product_type": "Cash"
}, separators=(',', ':'))

checksum = hashlib.sha256((time_stamp+payload+secret_key).encode("utf-8")).hexdigest()
headers = {
    'Content-Type': 'application/json',
    'X-Checksum': 'token '+ checksum,
    'X-Timestamp': time_stamp,
    'X-AppKey': appkey,
    'X-SessionToken': session_token
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)