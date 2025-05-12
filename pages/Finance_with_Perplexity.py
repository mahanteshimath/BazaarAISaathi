import streamlit as st
from utils.finance_utils import get_top_10_learnings, ask_finance_question, load_books
import pandas as pd

if "learnings" not in st.session_state:
    st.session_state["learnings"] = None
if "answer" not in st.session_state:
    st.session_state["answer"] = None

st.title("Finance with Perplexity")
st.subheader("Select and Read any book related to Finance")

# Load books data
books_file_path = "./src/Top50Books.csv"
books_data = load_books(books_file_path)

if "error" in books_data:
    st.error(books_data["error"])
else:
    st.write("### Select a Book")
    book_names = books_data["Book Name"].tolist()
    selected_book = st.selectbox("Choose a book to summarize its top 10 learnings:", book_names)

    if st.button("Summarize Top 10 Learnings"):
        with st.spinner("Fetching top 10 learnings..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            learnings = get_top_10_learnings(selected_book, api_key)

            if isinstance(learnings, dict) and "error" in learnings:
                st.error(f"Error: {learnings['error']}")
            else:
                st.session_state["learnings"] = learnings

    if st.session_state["learnings"]:
        st.subheader(f"Top 10 Learnings from '{selected_book}'")
        st.write(st.session_state["learnings"])

st.write("-----")
st.write("### Ask any Finance Question")
question = st.text_area("Enter your finance-related question i.e What is the current stock price of BSE?",height=100)

if st.button("Get Answer"):
    with st.spinner("Fetching answer..."):
        api_key = st.secrets["PERPLEXITY_API_KEY"]
        answer = ask_finance_question(question, api_key)

        if "error" in answer:
            st.error(f"Error: {answer['error']}")
        else:
            st.session_state["answer"] = answer

if st.session_state["answer"]:
    st.subheader("Answer")
    st.write(st.session_state["answer"])

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