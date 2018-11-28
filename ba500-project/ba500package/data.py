import os
from urllib.request import urlretrieve
import pandas as pd

Montgomery_URL = 'https://data.montgomerycountymd.gov/api/views/4mse-ku6q/rows.csv?accessType=DOWNLOAD'

def get_county_data(filename='data/Traffic_Violations.csv', url=Montgomery_URL, force_download=False):

    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    df = pd.read_csv('data/Traffic_Violations.csv', index_col=[0], parse_dates=[[0,1]])
    return df