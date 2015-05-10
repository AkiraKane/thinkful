"""
Utility functions for manipulating the Lending Club data set in Unit 2
"""
import os
import pandas as pd

def fetch_data_frame(filename='loansData.csv'):
    """
    Loads the Lending Club data with some minimal scrubbing
    :return:a pandas data frame
    """
    # load and scrub data
    data_filepath = os.path.join('data', filename)
    loans_data = pd.read_csv(data_filepath, low_memory=False)
    loans_data.dropna(inplace=True)
    return loans_data

def fetch_and_prep_data_frame():
    """
    A convenience method to clean the data before use
    :return: a pandas data frame
    """
    loans_data = fetch_data_frame()
    scrub_interest_rate(loans_data)
    add_FICO_score(loans_data)
    add_interest_rate_below_12(loans_data)
    add_intercept(loans_data)
    return loans_data

def fetch_large_dataset():
    """
    Load the full lending club data set and scrub it
    :return: a pandas data frame
    """
    #loans_data = fetch_data_frame('sample.csv')
    loans_data = fetch_data_frame('LoanStats3c.csv')
    scrub_interest_rate(loans_data, 'int_rate')
    add_home_ownership(loans_data)
    return loans_data

def add_home_ownership( df ):
    """
    scrub the home_ownership field into a simplified boolean column
    :param df: a pandas data frame
    :return:
    """
    df['owns'] = map( lambda x: x != 'RENT', df['home_ownership'])


def get_low_FICO_score(score):
    """
    :param score: a FICO range, in the format low_num-high_num
    :return: the low number as an int
    """
    (low, high) = score.split('-')
    return int(low)


def scrub_interest_rate(df, column_name='Interest.Rate'):
    """
    Converts the interest rate column from "value%" back to floats
    :param df: a pandas data frame
    :return: pandas data frame, Interest.Rate column cleaned up in place
    """
    # JR - took the tutorial's suggestion to round
    df[column_name] = map( lambda x: round(float(x.rstrip('%'))/100, 4),
                               df[column_name])

def add_FICO_score( df ):
    """
    Adds a FICO score column to the data frame
    :param df: a pandas data frame
    :return:
    """
    df['FICO.Score'] = map( lambda x: get_low_FICO_score(x), df['FICO.Range'])

def add_interest_rate_below_12( df ):
    """
    Adds a column signifying whether the interest rate is < 12%
    :param df: a pandas data frame
    :return:
    """
    df['Interest.below12'] = map(lambda x: x < .12, df['Interest.Rate'])

def add_intercept( df ):
    """
    Adds a column signifying whether the interest rate is < 12%
    :param df: a pandas data frame
    :return:
    """
    df['Intercept'] = map(lambda x: 1, df['Interest.Rate'])

