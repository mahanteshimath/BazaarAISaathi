import streamlit as st
import streamlit.components.v1 as components

st.title("🗺️ Application Architecture")

# Use the correct relative path for Streamlit static file serving
st.image("src/App_Architecture.jpg", caption="BazaarAISaathi - High Level Architecture", use_container_width=True)

st.markdown(
    """
    ### How BazaarAISaathi Works
    
    **BazaarAISaathi** is designed to empower retail investors by integrating real-time stock data, advanced AI models, and user-friendly analytics in a seamless workflow:
    
    - **Data Ingestion:** Real-time stock data is fetched from sources like ICICI Direct and other market feeds.
    - **Modular Analysis:** The app is divided into modules for Indian Stock Market insights, Stock Analysis (Techno-Funda, Deep Research, Tip Tester), and Portfolio Optimization (including FIRE planning).
    - **AI-Powered Processing:** Each module leverages specialized AI models (Sonar family) for deep research, reasoning, and financial analysis. These models process user queries, uploaded tips, and portfolio data.
    - **Result Formatting:** All AI/ML outputs (in JSON) are converted into user-friendly formats and visualizations.
    - **Streamlit Frontend:** The results are presented in an interactive, visually appealing web interface, making complex analytics accessible to all users.
    
    > **Key Strength:** The architecture is modular and scalable, allowing easy integration of new data sources, models, and features as the platform evolves.
    """
)

# Load the HTML content from the file
with open("./src/Architecture_app.txt", "r") as file:
    html_content = file.read()

components.html(html_content, width=1000, height=600)

st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: blue;
        color: white;
    }
    .streamlit-expanderContent {
        background-color: blue;
        color: white;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

footer = """
<style>
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
st.markdown(footer, unsafe_allow_html=True)