import streamlit as st

_SESSION_API_KEY = "perplexity_api_key"
_SESSION_INPUT_KEY = "perplexity_api_key_input"


def get_perplexity_api_key(show_warning: bool = False) -> str:
    """Return the Perplexity API key from session state only."""
    api_key = st.session_state.get(_SESSION_API_KEY, "").strip()

    if show_warning and not api_key:
        st.warning("Perplexity features are disabled until you enter your API key in the sidebar.")

    return api_key


def render_perplexity_api_key_input() -> None:
    """Render sidebar controls to set or clear the Perplexity API key for this session."""
    st.sidebar.subheader("Perplexity API Key")

    if _SESSION_INPUT_KEY not in st.session_state:
        st.session_state[_SESSION_INPUT_KEY] = st.session_state.get(_SESSION_API_KEY, "")

    entered_key = st.sidebar.text_input(
        "Enter Perplexity API Key",
        type="password",
        key=_SESSION_INPUT_KEY,
        placeholder="pplx-...",
        help="Saved only for this running session.",
    ).strip()

    if entered_key:
        st.session_state[_SESSION_API_KEY] = entered_key

    if st.sidebar.button("Clear Perplexity Key", key="clear_perplexity_api_key"):
        st.session_state.pop(_SESSION_API_KEY, None)
        st.session_state[_SESSION_INPUT_KEY] = ""
        st.rerun()

    if st.session_state.get(_SESSION_API_KEY):
        st.sidebar.caption("Perplexity API key is set for this session.")
    else:
        st.sidebar.caption("No key set. Perplexity-powered features are disabled.")
