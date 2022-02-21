import streamlit as st

from fourwiki.lib import try_me

st.title('View some four wiki page')

st.button('HERE')

if st.button('HERE'):
    try_me()
