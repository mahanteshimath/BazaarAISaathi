import streamlit as st


st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)

st.set_page_config(
  page_title="BAZAARAISAATHI",
  page_icon="🇮🇳",
  layout="wide",
  initial_sidebar_state="expanded",
) 

# --- Info ---
Hypothesis_page = st.Page(
    "pages/Hypothesis.py",
    title="Hypothesis",
    icon=":material/cognition:",
    default=True,
)
Architecture_page = st.Page(
    "pages/Architecture.py",
    title="Architecture",
    icon=":material/home:",
)
# --- Projects ---
Indicators = st.Page(
    "pages/Market_Indicators.py",
    title="Market Indicators",
    icon=":material/analytics:",
)

Finance_with_Perplexity = st.Page(
    "pages/Finance_with_Perplexity.py",
    title="Finance with Perplexity",
    icon=":material/money_off:",
)

Techno_Fund_Analysis = st.Page(
    "pages/Techno_Fund_Analysis.py",
    title="Techno-Fund Analysis",
    icon=":material/finance:",
)
Deep_Research = st.Page(
    "pages/Deep_Research.py",
    title="Deep Research",
    icon=":material/research:",
)
Tip_Tester = st.Page(
    "pages/Tip_Tester.py",
    title="Tip Tester",
    icon=":material/lightbulb:",
)

Portfolio_Analysis = st.Page(
    "pages/Portfolio_Analysis.py",
    title="Portfolio Analysis and Optimization",
    icon=":material/analytics:",
)


pg = st.navigation(
    {
        "Info": [Hypothesis_page,Architecture_page],
        "Indian Stock market": [Indicators,Finance_with_Perplexity],
        "Stock Analysis": [Techno_Fund_Analysis,Deep_Research,Tip_Tester],
        "Portfolio": [Portfolio_Analysis],

    }
)


pg.run()
