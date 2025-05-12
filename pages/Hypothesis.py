import streamlit as st



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
st.markdown('<div class="flashing-title">❄️BAAZAR-AI-SAATHI❄️</div>', unsafe_allow_html=True)


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("./src/India.jpeg")

with col2:
    st.title("Hypothesis", anchor=False)
    st.write(
        """
        This section explores various hypotheses related to the Indian stock market, stock analysis, and portfolio management. 
        The goal is to provide insights and validate assumptions using data-driven approaches.
        """
    )
    st.subheader("Indian Stock Market")
    st.write(
        """
        - Analyze market indicators to understand trends and patterns.
        - Explore the impact of macroeconomic factors on stock performance.
        """
    )
    st.subheader("Stock Analysis")
    st.write(
        """
        - Perform fundamental and technical analysis to identify potential investment opportunities.
        - Test the effectiveness of stock tips and strategies.
        """
    )
    st.subheader("Portfolio")
    st.write(
        """
        - Optimize portfolio allocation to maximize returns and minimize risks.
        - Analyze portfolio performance over time.
        """
    )
st.markdown("""---------------------------------""")
st.write("\n")

st.write("\n")


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
