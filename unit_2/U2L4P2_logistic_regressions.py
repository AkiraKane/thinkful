__author__ = 'jriley'
#
'''
We only need to do a few more things to the data to get it ready for logistic regression.

* Create a new file called 'logistic_regression.py'. For this lesson, we're going to need pandas and statsmodels.
* Load the data.
* Add a column to your dataframe indicating whether the interest rate is < 12%.
* Do some spot checks to make sure that it worked.
    df[df['Interest.Rate'] == 10].head() # should all be True
    df[df['Interest.Rate'] == 13].head() # should all be False
* Statsmodels needs an intercept column in your dataframe, so add a column with a constant intercept of 1.0.
* Create a list of the column names of our independent variables,
  including the intercept, and call it ind_vars.

'''

import numpy as np
import statsmodels.api as sm
import lending_club_utils as utils


# load and scrub
loans_data = utils.fetch_and_prep_data_frame()


# Spot-check the results
# print (loans_data[loans_data['Interest.below12'] < 0.12]).head()
# print (loans_data[loans_data['Interest.below12'] >= 0.12]).head()

# Too much reading! Let's make this easier:
#for index, row in loans_data.iterrows():
#    assert(row['Interest.below12'] == (row['Interest.Rate'] < .12))

#print loans_data.keys()
# JR: not sure which ones are independent variables
# Looks like these two, from the next page:
ind_vars = ['FICO.Score','Interest.Rate']

logit = sm.Logit(loans_data['Interest.below12'], loans_data[ind_vars])
result = logit.fit()
coeff = result.params
print coeff
