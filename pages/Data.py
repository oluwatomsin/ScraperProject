import streamlit as st
from utils.module import data_loader

st.markdown("## Data Sourcing Page")
st.write("This pages is where the data scraping happens, All we need is a button that load the data from a specific "
         "webpage")


df = data_loader()

st.dataframe(df.head(5))
