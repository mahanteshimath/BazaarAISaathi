import streamlit as st
from utils.deep_research import perform_market_analysis

st.title("Deep Researches on Indian Stocks, Sectors and different perspectives")
st.write(
    """
    This page provides a comprehensive overview of various research topics related to the Indian stock market. 
    The topics are categorized into different sections for better understanding and usability.
    """
)
st.write("-----")
st.title("1.Market Analysis for a Specific Industry")

r1_expander = st.expander("Prompt Template", expanded=True)
r1_expander.markdown("""Prompt Template: I am [mention the problem you're facing in detail with background context].
Conduct an in-depth market analysis of the [industry name] industry in [region/country].
Include information on market size, key players, emerging trends, growth drivers, challenges, and future projections for the next [X] years. Provide data-backed insights and cite all sources. I want you to [mention how you want the output in detail with examples].
""")
r2_expander = st.expander("Prompt Example : Fully developed investor-focused market research prompt :")

r2_expander.markdown(""" 
> I am an angel investor considering funding a startup in the **electric two-wheeler** (e-scooters, e-bikes, etc.) ecosystem, but I am struggling to evaluate the market's maturity, competition, and long-term opportunity in this space.
> Conduct an **in-depth market analysis** of the **electric two-wheeler industry** in **Southeast Asia**.
> Include information on:
> 1. **Market size** (current and historical figures, segmented by country if possible)
> 2. **Recent growth rates** and **adoption curves**
> 3. **Key players** (OEMs, battery tech startups, ride-sharing platforms, etc.) and their **market share**
> 4. **Emerging trends** (e.g., battery swapping, subscription models, local manufacturing incentives)
> 5. **Growth drivers** (e.g., urbanization, government subsidies, climate policy, fuel prices)
> 6. **Challenges** (e.g., charging infrastructure, regulation, consumer trust, cost barriers)
> 7. **Future projections** for the next **5 years**
>
> Provide **data-backed insights** using the latest available sources and **cite all sources** clearly (with hyperlinks where possible).
>
> I want the output as a **professional market research report**, structured as follows:
>
> 1. **Executive Summary**
> 2. **Market Overview & Size**
> 3. **Competitive Landscape**
> 4. **Trends & Innovations**
> 5. **Market Drivers and Barriers**
> 6. **5-Year Forecast & Opportunities**
> 7. **Conclusion & Investment Implications**
>
> Use **headings**, **bullet points**, and **charts/tables** where applicable. Present it in a format suitable for use in a pitch deck or investor memorandum.

""")

# Add a button to copy the text
prompt_text = """I am an angel investor considering funding a startup in the electric two-wheeler (e-scooters, e-bikes, etc.) ecosystem, but I am struggling to evaluate the market's maturity, competition, and long-term opportunity in this space.
Conduct an in-depth market analysis of the electric two-wheeler industry in Southeast Asia.
Include information on:
1. Market size (current and historical figures, segmented by country if possible)
2. Recent growth rates and adoption curves
3. Key players (OEMs, battery tech startups, ride-sharing platforms, etc.) and their market share
4. Emerging trends (e.g., battery swapping, subscription models, local manufacturing incentives)
5. Growth drivers (e.g., urbanization, government subsidies, climate policy, fuel prices)
6. Challenges (e.g., charging infrastructure, regulation, consumer trust, cost barriers)
7. Future projections for the next 5 years

Provide data-backed insights using the latest available sources and cite all sources clearly (with hyperlinks where possible).

I want the output as a professional market research report, structured as follows:

1. Executive Summary
2. Market Overview & Size
3. Competitive Landscape
4. Trends & Innovations
5. Market Drivers and Barriers
6. 5-Year Forecast & Opportunities
7. Conclusion & Investment Implications

Use headings, bullet points, and charts/tables where applicable. Present it in a format suitable for use in a pitch deck or investor memorandum."""

if st.button('Copy Prompt to Clipboard'):
    st.write('Prompt copied to clipboard!')
    st.code(prompt_text)
st.write("-----")
st.text_area("Submit your Market Analysis prompt", key="user_prompt", height=200, placeholder="Type your prompt here...")

if st.button("Run Market Analysis", key="run_market_analysis"):
    user_prompt = st.session_state.get("user_prompt", "")
    if user_prompt:
        with st.spinner("Performing market analysis..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            analysis_result = perform_market_analysis(user_prompt, api_key)

            if isinstance(analysis_result, dict) and "error" in analysis_result:
                st.error(f"Error: {analysis_result['error']}")
            elif isinstance(analysis_result, dict):
                st.subheader("Market Analysis Result")
                st.write(analysis_result.get("content", "No content available"))

                citations = analysis_result.get("citations", [])
                if citations:
                    st.subheader("Citations")
                    for i, citation in enumerate(citations):
                        st.write(f"{i+1}. {citation}")
            else:
                st.warning("Unexpected response format.")
    else:
        st.warning("Please enter a prompt before running the analysis.")

st.write("-----")

st.title("2. Competitor Benchmarking")

r3_expander = st.expander("Prompt Template", expanded=True)
r3_expander.markdown("""Prompt Template: I am [mention the problem you're facing in detail with background context].
Create a competitor benchmarking report for [company name] in the [industry name] sector.
Compare it with [list of competitor names] based on financial performance, market share, product offerings, pricing strategies, and customer satisfaction.
Include visualizations like tables or charts where applicable. I want you to [mention how you want the output in detail with examples].""")

# Add a text area for user input
competitor_prompt_text = """I am [mention the problem you're facing in detail with background context].\nCreate a competitor benchmarking report for [company name] in the [industry name] sector.\nCompare it with [list of competitor names] based on financial performance, market share, product offerings, pricing strategies, and customer satisfaction.\nInclude visualizations like tables or charts where applicable. I want you to [mention how you want the output in detail with examples]."""

if st.button('Copy Competitor Benchmarking Prompt to Clipboard'):
    st.write('Prompt copied to clipboard!')
    st.code(competitor_prompt_text)

st.text_area("Submit your competitor benchmarking prompt", key="competitor_prompt", height=200, placeholder="Type your competitor benchmarking prompt here...")

if st.button("Run Competitor Benchmarking", key="run_competitor_benchmarking"):
    competitor_prompt = st.session_state.get("competitor_prompt", "")
    if competitor_prompt:
        with st.spinner("Performing competitor benchmarking..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            benchmarking_result = perform_market_analysis(competitor_prompt, api_key)

            if isinstance(benchmarking_result, dict) and "error" in benchmarking_result:
                st.error(f"Error: {benchmarking_result['error']}")
            elif isinstance(benchmarking_result, dict):
                st.subheader("Competitor Benchmarking Result")
                st.write(benchmarking_result.get("content", "No content available"))

                citations = benchmarking_result.get("citations", [])
                if citations:
                    st.subheader("Citations")
                    for i, citation in enumerate(citations):
                        st.write(f"{i+1}. {citation}")
            else:
                st.warning("Unexpected response format.")
    else:
        st.warning("Please enter a prompt before running the benchmarking.")

st.write("-----")

st.title("3. Investment Opportunity Evaluation")

r4_expander = st.expander("Prompt Template", expanded=True)
r4_expander.markdown("""Prompt Template: I am [mention the problem you're facing in detail with background context].
Evaluate the investment potential of [specific asset/sector/company]. Analyze its current performance, historical trends, risk factors, competitive landscape, and growth opportunities. Provide a recommendation based on your findings and include supporting data or case studies. I want you to [mention how you want the output in detail with examples].""")

# Add a text area for user input
investment_prompt_text = """I am [mention the problem you're facing in detail with background context].\nEvaluate the investment potential of [specific asset/sector/company]. Analyze its current performance, historical trends, risk factors, competitive landscape, and growth opportunities. Provide a recommendation based on your findings and include supporting data or case studies. I want you to [mention how you want the output in detail with examples]."""

if st.button('Copy Investment Opportunity Evaluation Prompt to Clipboard'):
    st.write('Prompt copied to clipboard!')
    st.code(investment_prompt_text)

st.text_area("Submit your investment opportunity evaluation prompt", key="investment_prompt", height=200, placeholder="Type your investment opportunity evaluation prompt here...")

if st.button("Run Investment Opportunity Evaluation", key="run_investment_evaluation"):
    investment_prompt = st.session_state.get("investment_prompt", "")
    if investment_prompt:
        with st.spinner("Evaluating investment opportunity..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            investment_result = perform_market_analysis(investment_prompt, api_key)

            if isinstance(investment_result, dict) and "error" in investment_result:
                st.error(f"Error: {investment_result['error']}")
            elif isinstance(investment_result, dict):
                st.subheader("Investment Opportunity Evaluation Result")
                st.write(investment_result.get("content", "No content available"))

                citations = investment_result.get("citations", [])
                if citations:
                    st.subheader("Citations")
                    for i, citation in enumerate(citations):
                        st.write(f"{i+1}. {citation}")
            else:
                st.warning("Unexpected response format.")
    else:
        st.warning("Please enter a prompt before running the evaluation.")

st.write("-----")

st.title("4. Technology Trends Report")

r5_expander = st.expander("Prompt Template", expanded=True)
r5_expander.markdown("""Prompt Template: I am [mention the problem you're facing in detail with background context].
Prepare a detailed report on the latest technology trends in [specific field, e.g., artificial intelligence, blockchain, renewable energy].
Include key innovations, adoption rates, potential applications, challenges to implementation, and predictions for the next $[X]$ years. I want you to [mention how you want the output in detail with examples].""")

# Add a text area for user input
tech_trends_prompt_text = """I am [mention the problem you're facing in detail with background context].\nPrepare a detailed report on the latest technology trends in [specific field, e.g., artificial intelligence, blockchain, renewable energy].\nInclude key innovations, adoption rates, potential applications, challenges to implementation, and predictions for the next $[X]$ years. I want you to [mention how you want the output in detail with examples]."""

if st.button('Copy Technology Trends Report Prompt to Clipboard'):
    st.write('Prompt copied to clipboard!')
    st.code(tech_trends_prompt_text)

st.text_area("Submit your technology trends report prompt", key="tech_trends_prompt", height=200, placeholder="Type your technology trends report prompt here...")

if st.button("Run Technology Trends Report", key="run_technology_trends"):
    tech_trends_prompt = st.session_state.get("tech_trends_prompt", "")
    if tech_trends_prompt:
        with st.spinner("Generating technology trends report..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            tech_trends_result = perform_market_analysis(tech_trends_prompt, api_key)

            if isinstance(tech_trends_result, dict) and "error" in tech_trends_result:
                st.error(f"Error: {tech_trends_result['error']}")
            elif isinstance(tech_trends_result, dict):
                st.subheader("Technology Trends Report Result")
                st.write(tech_trends_result.get("content", "No content available"))

                citations = tech_trends_result.get("citations", [])
                if citations:
                    st.subheader("Citations")
                    for i, citation in enumerate(citations):
                        st.write(f"{i+1}. {citation}")
            else:
                st.warning("Unexpected response format.")
    else:
        st.warning("Please enter a prompt before running the report.")

st.write("-----")

st.title("5. Marketing Strategy Development")

r6_expander = st.expander("Prompt Template", expanded=True)
r6_expander.markdown("""Prompt Template: I am [mention the problem you're facing in detail with background context].
Develop a comprehensive marketing strategy for [product/service] targeting [specific audience].
Include insights on market segmentation, customer personas, messaging strategies, channel recommendations (e.g., social media, email), and measurable KPIs to track success. I want you to [mention how you want the output in detail with examples].""")

# Add a text area for user input
marketing_strategy_prompt_text = """I am [mention the problem you're facing in detail with background context].\nDevelop a comprehensive marketing strategy for [product/service] targeting [specific audience].\nInclude insights on market segmentation, customer personas, messaging strategies, channel recommendations (e.g., social media, email), and measurable KPIs to track success. I want you to [mention how you want the output in detail with examples]."""

if st.button('Copy Marketing Strategy Development Prompt to Clipboard'):
    st.write('Prompt copied to clipboard!')
    st.code(marketing_strategy_prompt_text)

st.text_area("Submit your marketing strategy development prompt", key="marketing_strategy_prompt", height=200, placeholder="Type your marketing strategy development prompt here...")

if st.button("Run Marketing Strategy Development", key="run_marketing_strategy"):
    marketing_strategy_prompt = st.session_state.get("marketing_strategy_prompt", "")
    if marketing_strategy_prompt:
        with st.spinner("Developing marketing strategy..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            marketing_strategy_result = perform_market_analysis(marketing_strategy_prompt, api_key)

            if isinstance(marketing_strategy_result, dict) and "error" in marketing_strategy_result:
                st.error(f"Error: {marketing_strategy_result['error']}")
            elif isinstance(marketing_strategy_result, dict):
                st.subheader("Marketing Strategy Development Result")
                st.write(marketing_strategy_result.get("content", "No content available"))

                citations = marketing_strategy_result.get("citations", [])
                if citations:
                    st.subheader("Citations")
                    for i, citation in enumerate(citations):
                        st.write(f"{i+1}. {citation}")
            else:
                st.warning("Unexpected response format.")
    else:
        st.warning("Please enter a prompt before running the strategy development.")

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