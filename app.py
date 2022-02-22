import streamlit as st

from fourwiki.lib import try_me

st.title('View some four wiki page')

click = st.button('HERE')

if click:
    link, status_text = try_me()
    st.markdown(link, unsafe_allow_html=True)
    st.write(status_text)
