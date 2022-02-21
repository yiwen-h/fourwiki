import streamlit as st

from fourwiki.lib import try_me

st.title('View some four wiki page')

if st.button('HERE'):
    print(try_me())
