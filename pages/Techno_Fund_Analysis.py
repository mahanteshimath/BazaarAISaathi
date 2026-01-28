import streamlit as st
import pandas as pd
from langchain import PromptTemplate, LLMChain
from langchain_community.chat_models.perplexity import ChatPerplexity
from langchain.chains import SequentialChain

# Load NSE_EQUITYS.csv file
file_path = "./src/NSE_EQUITYS.csv"
try:
    nse_data = pd.read_csv(file_path)
    company_names = nse_data["NAME OF COMPANY"].tolist()

    st.title("Techno Fundamental Analysis")
    st.write("### Select a Company")

    selected_company = st.selectbox("Choose a company for analysis:", company_names)

    # -------------------- Initialization --------------------
    # API key and model initialization
    llm = ChatPerplexity(model="sonar-reasoning-pro", 
                        #  temperature=0.5, 
                         pplx_api_key=st.secrets["PERPLEXITY_API_KEY"])

    # -------------------- Chain Definitions --------------------
    # Define all chains globally
    market_data_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["Listed_Name"],
            template=(
                "Act as an Experienced sucessful/profitable Indian stock market investor. Provide a comprehensive analysis of the given {Listed_Name}. This should include a thorough evaluation of the company financial health, its competitive position in the industry, and any macroeconomic factors that could impact its performance. The analysis should also include an assessment of the stock's valuation, taking into account its projected earnings growth and other key financial metrics. Based on your analysis, provide a recommendation on whether to buy, hold, or sell the stock. Your analysis should be backed with supporting data and reasoning."
                "📈 For {Listed_Name}, provide detailed and up-to-date financial data. Include current stock price, "
                "volume, key financial ratios (e.g., P/E, P/B, dividend yield), recent price trends, and relevant market indicators."
                "Do not add any disclaimer that I am not a SEBI-registered investment advisor or AI-generated content"
                "Because explicitly I have informed users."
            
            
            )
        ),
        output_key="market_data"
    )

    sentiment_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["Listed_Name"],
            template=(
                "Act as an Experienced sucessful/profitable Indian stock market investor.. Provide a comprehensive analysis of the given {Listed_Name}. This should include a thorough evaluation of the company financial health, its competitive position in the industry, and any macroeconomic factors that could impact its performance. The analysis should also include an assessment of the stock's valuation, taking into account its projected earnings growth and other key financial metrics. Based on your analysis, provide a recommendation on whether to buy, hold, or sell the stock. Your analysis should be backed with supporting data and reasoning."
                "Also For {Listed_Name}, analyze recent news articles, social media posts, and expert commentary. "
                "Summarize the prevailing sentiment, highlight any key events, and note emerging trends that may impact the stock."
                "Do not add any disclaimer that I am not a SEBI-registered investment advisor or AI-generated content"
                "Because explicitly I have informed users."
            )
        ),
        output_key="sentiment_analysis"
    )

    macro_analysis_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["Listed_Name"],
            template=(
                "Act as an Experienced sucessful/profitable Indian stock market investor. 🌐 For {Listed_Name}, analyze the current macro-economic environment. "
                "Include key indicators such as GDP growth, inflation rates, interest rates, unemployment trends, "
                "and central bank policies. Summarize how these factors could impact the overall market and the asset."
                "Do not add any disclaimer that I am not a SEBI-registered investment advisor or AI-generated content"
                "Because explicitly I have informed users."
            )
        ),
        output_key="macro_analysis"
    )

    strategy_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["market_data", "sentiment_analysis", "macro_analysis"],
            template=(
                "Act as an Experienced sucessful/profitable Indian stock market investor.📊 Using the detailed market data:\n{market_data}\n"
                "the sentiment analysis:\n{sentiment_analysis}\n"
                "and the macro-economic analysis:\n{macro_analysis}\n"
                "develop a sophisticated trading strategy. Outline a clear asset allocation, specify entry and exit points, "
                "detail risk management measures, and provide estimated expected returns. If applicable, incorporate algorithmic signals."
                "Do not add any disclaimer that I am not a SEBI-registered investment advisor or AI-generated content"
                "Because explicitly I have informed users."
            )
        ),
        output_key="strategy"
    )

    risk_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["strategy"],
            template=(
                "Act as an Experienced sucessful/profitable Indian stock market investor. ⚠️ Evaluate the following trading strategy:\n{strategy}\n"
                "Identify potential risks such as market volatility, liquidity issues, or unexpected market events. "
                "Summarize your risk assessment in 4 concise bullet points, and state in the final bullet point whether the strategy meets an acceptable risk tolerance.  At the end of analysis recommend with BUY at PRICE , SELL At Pirce or HOLD. "
                "Do not add any disclaimer that I am not a SEBI-registered investment advisor or AI-generated content"
                "Because explicitly I have informed users."
            )
        ),
        output_key="risk_assessment"
    )

    # Define the `sequential_agent` globally
    sequential_agent = SequentialChain(
        chains=[market_data_chain, sentiment_chain, macro_analysis_chain, strategy_chain, risk_chain],
        input_variables=["Listed_Name"],
        output_variables=["market_data", "sentiment_analysis", "macro_analysis", "strategy", "risk_assessment"],
        verbose=True
    )

    if selected_company:
        company_info = nse_data[nse_data["NAME OF COMPANY"] == selected_company].iloc[0]
        symbol = company_info["SYMBOL"]
        listed_name = f"{symbol}:{selected_company}"
        st.write(f"**Selected Company:** {listed_name}")

        if st.button("Do Through Fundamental Analysis"):
            def run_ai_hedge_fund(listed_name: str) -> None:
                result = sequential_agent({"Listed_Name": listed_name})

                st.title("📈 Market Data Retrieved:")
                st.write("--------------------------------------------------")
                st.write(result["market_data"], "\n")

                st.title("📰 Market Sentiment Analysis:")
                st.write("--------------------------------------------------")
                st.write(result["sentiment_analysis"], "\n")

                st.title("🌐 Macro-Economic Analysis:")
                st.write("--------------------------------------------------")
                st.write(result["macro_analysis"], "\n")

                st.title("📊 Developed Trading Strategy:")
                st.write("--------------------------------------------------")
                st.write(result["strategy"], "\n")

                st.title("⚠️ Risk Assessment:")
                st.write("--------------------------------------------------")
                st.write(result["risk_assessment"], "\n")

                st.write("==============================================\n")

            run_ai_hedge_fund(listed_name)

except Exception as e:
    st.error(f"Failed to load NSE data: {str(e)}")

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