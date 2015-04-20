import os
import pandas as pd


def fetch_data_frame():
    # load and scrub data
    data_filepath = os.path.join('data', 'loansData.csv')
    loans_data = pd.read_csv(data_filepath)
    loans_data.dropna(inplace=True)
    return loans_data