'''
https://courses.thinkful.com/data-001v2/assignment/2.6.2

'''
import pandas as pd
import numpy as np
import lending_club_utils as utils

df = utils.fetch_timeseries_dataset()
dfts = df.set_index('issue_d_format')

# converts string to datetime object in pandas:
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']
print loan_count_summary