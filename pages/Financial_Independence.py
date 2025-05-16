import streamlit as st
from utils.deep_research import perform_market_analysis

st.title("Financial Independence")

st.header("FIRE (Financial Independence, Retire Early) Planner")

st.markdown("""
Enter your scenario or question below. For example:
- "Create a detailed plan for achieving financial independence within a 10-year timeframe on a salary of 50,000 rupees per month. The plan should include specific savings goals, investment strategies, and potential side income sources. Provide a clear breakdown of monthly expenses, recommended savings percentage, and types of investments to consider, such as stocks, mutual funds, or real estate. Additionally, outline any skills that could be developed to increase earning potential over this period."
""")

fire_prompt = st.text_area("Ask your FIRE/financial independence question", key="fire_prompt", height=150, placeholder="Type your scenario or question here...")

if st.button("Run FIRE Planner", key="run_fire_planner"):
    if fire_prompt:
        with st.spinner("Generating your FIRE plan..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            fire_result = perform_market_analysis(fire_prompt, api_key)

            if isinstance(fire_result, dict) and "error" in fire_result:
                st.error(f"Error: {fire_result['error']}")
            elif isinstance(fire_result, dict):
                st.subheader("FIRE Plan Result")
                st.write(fire_result.get("content", "No content available"))
                citations = fire_result.get("citations", [])
                if citations:
                    st.subheader("Citations")
                    for i, citation in enumerate(citations):
                        st.write(f"{i+1}. {citation}")
            else:
                st.warning("Unexpected response format.")
    else:
        st.warning("Please enter a scenario or question before running the planner.")

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