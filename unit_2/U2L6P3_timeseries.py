'''
https://courses.thinkful.com/data-001v2/assignment/2.6.2

'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import lending_club_utils as utils
import statsmodels.api as sm


df = utils.fetch_timeseries_dataset()
#print df.info()
# Looks like there are a lot of columns unrelated to this question
# The loan count summary takes  a long time to appear. It makes me
# want to select only the values we need for the problem.

dfts = df.set_index('issue_d_format')
# converts string to datetime object in pandas:
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']
values = loan_count_summary.values
print loan_count_summary


# Challenges 1:
# Plot the loan data (loan_count_summary in from the previous assignment).
# Is the series stationary?
# If not, what would you do to transform it into a stationary series?
plt.plot(loan_count_summary.values)
plt.ylabel("Num Loans")
plt.xlabel("Month")
#plt.show()


# Challenge 2:
# Plot out the ACF (statsmodels.api.graphics.tsa.plot_acf())
# and PACF (statsmodels.api.graphics.tsa.plot_pacf())
# of the series (or the transformed series).
# Are there any autocorrelated structures in the series?
# How would you have a model address these structures?

from pandas.tools.plotting import autocorrelation_plot
autocorrelation_plot(loan_count_summary.values)
plt.show()

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
sm.graphics.tsa.plot_acf(values)


ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(values)
plt.show()
