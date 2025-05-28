import streamlit as st

# Add a logo and navigation link
st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)

def add_custom_css():
    st.markdown("""
        <style>
        .flashing-title {
            font-size: 1.7em;
            font-weight: bold;
            color: #4CAF50;
            animation: flash 2s infinite;
        }
        @keyframes flash {
            0% { opacity: 1; }
            30% { opacity: 0; }
            100% { opacity: 1; }
        }
        </style>
        """, unsafe_allow_html=True)

add_custom_css()
st.markdown('<div class="flashing-title">❄️WELCOME TO BAAZAR-AI-SAATHI ❄️</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("./src/India.jpeg")

with col2:
    st.title("Hypothesis", anchor=False)
    st.write(
        """
        BazaarAISaathi is built on the hypothesis that retail investors can dramatically improve their financial outcomes by leveraging AI-powered tools for:
        - Deep market analysis
        - Data-driven decision making
        - Personalized portfolio management
        
        Our mission is to democratize access to advanced financial intelligence, making the Indian stock market more transparent, accessible, and profitable for everyone.
        """
    )
    st.subheader("🔎 Indian Stock Market Insights")
    st.write(
        """
        - Analyze real-time and historical market indicators to uncover actionable trends.
        - Assess the impact of macroeconomic and sectoral factors on stock performance.
        - Deliver timely insights to help investors minimize risks and seize opportunities.
        """
    )
    st.subheader("📈 Stock & Strategy Analysis")
    st.write(
        """
        - Perform both fundamental and technical analysis using AI and data science.
        - Test and validate investment tips, strategies, and market hypotheses.
        - Provide unbiased, AI-powered recommendations to support informed decisions.
        """
    )
    st.subheader("💼 Portfolio Optimization")
    st.write(
        """
        - Optimize asset allocation for maximum returns and risk management.
        - Continuously monitor and analyze portfolio performance against financial goals.
        - Generate stock-wise and holistic recommendations to enhance portfolio health.
        """
    )
    st.subheader("🧠 Why AI for Investing?")
    st.write(
        """
        - AI can process vast amounts of financial data, news, and sentiment in real time.
        - It helps identify patterns and opportunities that are invisible to the human eye.
        - Personalized insights empower retail investors to compete with institutional players.
        """
    )

st.markdown("""---""")

st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: #2C1E5B;
        color: white;
    }
    .streamlit-expanderContent {
        background-color: #2C1E5B;
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
