import streamlit as st
from utils.module import data_loader
import plotly.express as px

# Loading out crude oil dataset
data = data_loader()

# Creating the figure for our chart
fig = px.line(data, x='Date', y='Closing Value', title='Closing price of Crude over time', width=1000, height=600)
st.plotly_chart(fig)
