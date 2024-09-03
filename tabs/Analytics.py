import streamlit as st
from utils.module import data_loader
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


# Loading out crude oil dataset
data = data_loader()
data_2 = data_loader(path='data/oil_prices_filtered.csv', skips=1)


@st.cache_resource
def display_line():
    """
    This function just creates a line plot the crude oil prices overtime
    :return: None
    """
    # Creating the figure for our chart
    fig = px.line(data, x='Date', y='Closing Value', title='Closing price of Crude over time', width=1000, height=600)
    date_buttons = [
        {'count': 1, 'step': 'year', 'stepmode': 'todate', 'label': 'YTD'},
        {'count': 6, 'step': 'month', 'stepmode': 'todate', 'label': '6MTD'},
        {'count': 7, 'step': 'day', 'stepmode': 'todate', 'label': 'WTD'}
    ]
    fig.update_layout(
        {'xaxis': {'rangeselector': {'buttons': date_buttons}}}
    )
    st.plotly_chart(fig)


@st.cache_resource
def display_bar(df=data_2):

    # here I'm adding a column with colors
    df["Color"] = np.where(df["Change"] < 0, 'red', 'green')

    # Create a subplot with 2 rows and 1 column
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    # Add the "Last Price of Commodity" bar plot to the first row
    fig.add_trace(
        go.Bar(x=df['Futures & Indexes'], y=df['Last'], name="Last Price of Commodity"),
        row=1, col=1
    )

    # Add the "% Change in Price of Commodity" bar plot to the second row with conditional coloring
    fig.add_trace(
        go.Bar(x=df['Futures & Indexes'], y=df['Change'], name="Change in Price of Commodity",
               marker_color=df['Color']),
        row=2, col=1
    )

    # Update layout
    fig.update_layout(
        title="Commodity Prices and Change in price",
        height=1000,  # Adjust height as needed
        width=3500  # Set the desired width

    )

    # Add titles to each subplot
    fig.update_yaxes(title_text="Last Price of Commodity", row=1, col=1)
    fig.update_yaxes(title_text="% Change in Price of Commodity", row=2, col=1)

    # Add curved borders using shapes (rounded rectangles)
    fig.add_shape(
        type="rect",
        x0=-0.5, y0=0.5, x1=25, y1=100,  # Adjust coordinates as needed
        xref="x", yref="y1",
        line=dict(color="RoyalBlue", width=2),
        fillcolor="LightSkyBlue",
        opacity=0.3,
        layer="below"
    )
    fig.add_shape(
        type="rect",
        x0=-0.5, y0=-2.5, x1=25, y1=3,  # Adjust coordinates as needed
        xref="x", yref="y2",
        line=dict(color="RoyalBlue", width=2),
        fillcolor="LightSkyBlue",
        opacity=0.3,
        layer="below"
    )

    st.plotly_chart(fig)


display_line()
display_bar()