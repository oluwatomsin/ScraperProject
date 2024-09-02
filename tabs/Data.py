import streamlit as st
import pandas as pd
from utils.module import extract_percentage, fetch_latest_data

st.markdown("## Data Sourcing Page")
st.write("This pages is where the data scraping happens, All we need is a button that load the data from a specific "
         "webpage")

df = pd.read_csv('./data/oil_prices_filtered.csv')
df = df.drop('Unnamed: 0', axis=1)
df = df.drop([0], axis = 0).reset_index(drop=True) 

df['% Change'] = df['% Change'].apply(extract_percentage)
st.dataframe(df)

if st.button("Update data from web"):
    fetch_latest_data()
    st.success("Data successfully updated")