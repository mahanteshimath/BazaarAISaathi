import streamlit as st
from utils.summariser import FinanceDocumentSummarizer

# Title of the app
st.title("Finance Document Summarizer")

# Initialize the summarizer
summarizer = FinanceDocumentSummarizer()

# Input for public document links
document_links = st.text_area("Enter public document links (separated by semicolons):", placeholder="https://www.bseindia.com/xml-data/corpfiling/AttachHis/03820485-8318-496e-845a-3c0f87ceceb0.pdf; extract info from this")

# Use API key from secrets
api_key = st.secrets["PERPLEXITY_API_KEY"]

if st.button("Summarize"):
    if not document_links:
        st.warning("Please provide document links.")
    elif not api_key:
        st.warning("API key is missing in secrets.")
    else:
        links = document_links.split(";")
        for link in links:
            link = link.strip()
            if link:
                st.subheader(f"Processing Link: {link}")
                try:
                    summary = summarizer.summarize_with_api(link, api_key)
                    if 'content' in summary:
                        st.markdown(f"### Summary for {link}")
                        st.markdown(summary['content'])
                    if 'citations' in summary and summary['citations']:
                        st.markdown("#### Citations:")
                        for citation in summary['citations']:
                            st.markdown(f"- {citation}")
                except Exception as e:
                    st.error(f"Error summarizing link {link}: {e}")

# Footer
footer = """<style>
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
