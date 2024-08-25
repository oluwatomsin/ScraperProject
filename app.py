import streamlit as st

st.markdown("# This page is dedicated to the demo")

st.write("For information about getting data, head over to the data page in the navigation bar and for analytics also. "
         "NB: This page is merely and sample and does not fully represent how the final page will appear however,"
         "all features in this demo will be present in the final application.")

st.Page('./pages/Data.py', title='Data', icon=":material/favorite:")
st.Page('./pages/Analytics.py', title='Analytics', icon=":material/favorite:")

