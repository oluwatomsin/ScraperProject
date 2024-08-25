import streamlit as st
import pandas as pd

st.markdown("## Data Sourcing Page")
st.write("This pages is where the data scraping happens, All we need is a button that load the data from a specific "
         "webpage")

df = pd.read_csv('./data/crude-oil-prices-daily.csv', skiprows=9)

st.dataframe(df.head(5))
