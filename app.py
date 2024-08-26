import streamlit as st

st.markdown("# Oil Prices Scraping and Analytics")


pg = st. navigation([
    st.Page('./pages/Data.py', title='Data', icon=":material/favorite:"),
    st.Page('./pages/Analytics.py', title='Analytics', icon=":material/favorite:")
])
pg.run()
