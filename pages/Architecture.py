import streamlit as st

import streamlit.components.v1 as components

# Load the HTML content from the file
with open("./src/Architecture_app.txt", "r") as file:
    html_content = file.read()

# Add zoom and fit functionality to the HTML content
html_with_zoom = f"""
<html>
<head>
<style>
  body {{
    margin: 0;
    padding: 0;
    overflow: hidden;
  }}
  iframe {{
    width: 100%;
    height: 100%;
    border: none;
    transform-origin: 0 0;
  }}
</style>
<script>
  function setZoom(scale) {{
    const iframe = document.getElementById('content-frame');
    iframe.style.transform = 'scale(' + scale + ')';
  }}
</script>
</head>
<body>
  <iframe id="content-frame" srcdoc="{html_content}" scrolling="auto"></iframe>
  <div style="position: fixed; bottom: 10px; right: 10px;">
    <button onclick="setZoom(1)">Fit</button>
    <button onclick="setZoom(1.5)">Zoom In</button>
    <button onclick="setZoom(0.75)">Zoom Out</button>
  </div>
</body>
</html>
"""

components.html(html_with_zoom, width=800, height=600)

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