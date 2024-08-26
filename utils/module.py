import pandas as pd
import streamlit as st


@st.cache_data
def data_loader(path: str = './data/crude-oil-prices-daily.csv', skips:int = 9) -> pd.DataFrame:
    df = pd.read_csv(path, skiprows=skips)
    return df

