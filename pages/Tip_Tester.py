import streamlit as st
from utils.tip_analysis import analyze_tip_or_advice

st.title("Tip or Investment Advice Tester")
st.write("This app allows you to test the performance of your investment advice or tip. You can input the details of your investment, including the amount, duration, and expected return. The app will then calculate the potential profit or loss based on your inputs.")

# Add input for text-based advice
tip_text = st.text_area("Enter your investment advice or tip", placeholder="Type your investment advice or tip here...")

# Add file uploader for screenshot of advice
uploaded_file = st.file_uploader("Upload a screenshot of your investment advice (optional)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Screenshot", use_column_width=True)

if tip_text or uploaded_file:
    st.success("Your investment advice or tip has been submitted successfully!")

# Add a button to run deep analysis for the tip or advice
if st.button("Run Deep Analysis for Tip or Advice"):
    if tip_text:
        with st.spinner("Analyzing your tip or advice..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            analysis_result = analyze_tip_or_advice(tip_text, api_key)

            if isinstance(analysis_result, dict) and "error" in analysis_result:
                st.error(f"Error: {analysis_result['error']}")
            elif isinstance(analysis_result, dict):
                st.subheader("Deep Analysis Result")
                st.write(analysis_result.get("content", "No content available"))
            else:
                st.warning("Unexpected response format.")
    else:
        st.warning("Please enter a tip or advice before running the analysis.")

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