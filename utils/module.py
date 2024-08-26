import pandas as pd
import streamlit as st
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

import re
import os


@st.cache_resource
def data_loader(path: str = './data/crude-oil-prices-daily.csv', skips:int = 9) -> pd.DataFrame:
    df = pd.read_csv(path, skiprows=skips)
    return df

def extract_percentage(text):
    match = re.search(r'([+-]?\d+\.?\d*)%', str(text))
    if match:
        return match.group(1) + '%'
    else:
        return 'N/A'  



def fetch_latest_data():
    """A function that will be tied to a button for getting the latest prices for crude oil"""

    load_dotenv()
    url = os.environ["URL"]  
    response = requests.get(url)

    if response.status_code == 200:
        # parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the first table on the page
        table = soup.find('table')
        
        headers = []
        header_row = table.find_all('th')
        if header_row:
            headers = [header.text.strip() for header in header_row]
        
        # Extract table rows
        rows = table.find_all('tr')
        table_data = []
        
        for row in rows:
            # Extract each cell in the row
            cells = row.find_all(['td', 'th'])
            row_data = [cell.text.strip() for cell in cells]
            table_data.append(row_data)
        
        # render the tables via dataframe for a better view
        df = pd.DataFrame(table_data, columns=headers if headers else None)
        
        # Save the DataFrame to a CSV file
        df.to_csv("./data/oil_prices_filtered.csv", index=False)
        
    else:
        st.write(f"Failed to retrieve the webpage. Status code: {response.status_code}")
