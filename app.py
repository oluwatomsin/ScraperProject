import streamlit as st

st.markdown("# Oil Prices Scraping and Analytics")

st.write("For information about getting data, head over to the data page in the navigation bar and for analytics also. "
         "NB: This page is merely and sample and does not fully represent how the final page will appear however,"
         "all features in this demo will be present in the final application.")

pg = st. navigation([
    st.Page('tabs/Data.py', title='Data', icon=":material/favorite:"),
    st.Page('tabs/Analytics.py', title='Analytics', icon=":material/favorite:")
])
pg.run()
