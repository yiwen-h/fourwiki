import streamlit as st

from fourwiki.lib import try_me

st.title('View some four wiki page')

click = st.button('HERE')

if click:
    result = try_me()
    st.write(result)
