import streamlit as st
from utils.fire_planner import generate_fire_plan

st.title("Financial Independence")

st.header("FIRE (Financial Independence, Retire Early) Planner")

with st.form("fire_form"):
    age = st.number_input("Your Age", min_value=18, max_value=100, value=30, step=1)
    salary = st.number_input("Monthly Salary (in rupees)", min_value=1000, max_value=1000000, value=50000, step=1000)
    years = st.number_input("Timeframe to achieve FIRE (years)", min_value=1, max_value=50, value=10)
    essentials = st.number_input("Monthly Essentials (in rupees)", min_value=0, max_value=1000000, value=25000, step=500)
    non_essentials = st.number_input("Monthly Non-Essentials (in rupees)", min_value=0, max_value=1000000, value=10000, step=500)
    savings_pct = st.slider("Recommended Savings Percentage (%)", min_value=1, max_value=90, value=30)
    investment_types = st.text_input("Types of Investments (e.g., stocks, mutual funds, real estate)", value="mutual funds, stocks, savings accounts")
    side_income = st.text_input("Potential Side Income Sources (comma separated)", value="freelancing, tutoring, online business")
    skills = st.text_input("Skills to Develop (comma separated)", value="coding, design, project management")
    submitted = st.form_submit_button("Run FIRE Planner")

if submitted:
    with st.spinner("Generating your FIRE plan..."):
        api_key = st.secrets["PERPLEXITY_API_KEY"]
        fire_result = generate_fire_plan(
            age, salary, years, essentials, non_essentials, savings_pct, investment_types, side_income, skills, api_key
        )
        if isinstance(fire_result, dict) and "error" in fire_result:
            st.error(f"Error: {fire_result['error']}")
        elif isinstance(fire_result, dict):
            st.subheader("FIRE Plan Result")
            content = fire_result.get("content", "No content available")
            # Split content into lines and render LaTeX where appropriate
            for line in content.splitlines():
                line = line.strip()
                if not line:
                    continue
                # Detect LaTeX block expressions
                if line.startswith("$$") and line.endswith("$$"):
                    st.latex(line[2:-2])
                elif line.startswith("$") and line.endswith("$"):
                    st.latex(line[1:-1])
                elif line.startswith("\\[") and line.endswith("\\]"):
                    st.latex(line[2:-2])
                elif line.startswith("\\(") and line.endswith("\\)"):
                    st.latex(line[2:-2])
                else:
                    st.markdown(line)
            citations = fire_result.get("citations", [])
            if citations:
                st.subheader("Citations")
                for i, citation in enumerate(citations):
                    st.write(f"{i+1}. {citation}")
        else:
            st.warning("Unexpected response format.")

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