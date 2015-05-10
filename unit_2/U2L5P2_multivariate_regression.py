'''
Multivariate analysis
https://courses.thinkful.com/data-001v2/project/2.5.2

Load the Lending Club Statistics.
Use income (annual_inc) to model interest rates (int_rate).
Add home ownership (home_ownership) to the model.
Does that affect the significance of the coefficients in the original model?
+ Try to add the interaction of home ownership and incomes as a term.
How does this impact the new model?
'''

import lending_club_utils as utils

import numpy as np
import pandas as pd
import statsmodels.api as sm

loan_data = utils.fetch_large_dataset()

# annual_inc
# home_ownership
# int_rate
# int_rate  = b + m (annual_inc)
# int_rate  = b + m (annual_inc) + n(home_ownership)
#  turned home_ownership into a 0 (RENT) or 1 ( MORTGAGE || OWN )


interest = loan_data['int_rate']
income = loan_data['annual_inc']
homeowner = loan_data['owns']

# Following the process and  naming conventions
#from the linear regression lesson, https://courses.thinkful.com/data-001v2/project/2.3.3

y = np.matrix(interest).transpose()
x1 = np.matrix(income).transpose()
x2 = np.matrix(homeowner).transpose()

# 2.3.3: "Now you want to put the two columns together to create an input matrix (with one column for each independent variable):"
#x = np.column_stack([x1, x2])
x = np.column_stack([x1, x2])

# 2.3.3: "Now we create a linear model:"
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print f.summary()

'''
Results from using x1 only in np.column_stack
/Users/me/anaconda/bin/python /Users/me/workspace/thinkful/unit_2/U2L5P2_multivariate_regression.py
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.003
Model:                            OLS   Adj. R-squared:                  0.002
Method:                 Least Squares   F-statistic:                     1.975
Date:                Sun, 10 May 2015   Prob (F-statistic):              0.160
Time:                        16:59:40   Log-Likelihood:                 1235.2
No. Observations:                 636   AIC:                            -2466.
Df Residuals:                     634   BIC:                            -2457.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
const          0.1470      0.002     58.810      0.000         0.142     0.152
x1          3.869e-08   2.75e-08      1.406      0.160     -1.54e-08  9.28e-08
==============================================================================
Omnibus:                       53.123   Durbin-Watson:                   1.970
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               66.941
Skew:                           0.696   Prob(JB):                     2.91e-15
Kurtosis:                       3.766   Cond. No.                     1.65e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.65e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

'''
'''
And here with x1 and x2 both:

/Users/me/anaconda/bin/python /Users/me/workspace/thinkful/unit_2/U2L5P2_multivariate_regression.py
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.008
Model:                            OLS   Adj. R-squared:                  0.005
Method:                 Least Squares   F-statistic:                     2.461
Date:                Sun, 10 May 2015   Prob (F-statistic):             0.0861
Time:                        17:00:43   Log-Likelihood:                 1236.7
No. Observations:                 636   AIC:                            -2467.
Df Residuals:                     633   BIC:                            -2454.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
const          0.1495      0.003     51.685      0.000         0.144     0.155
x1          4.473e-08   2.77e-08      1.614      0.107     -9.69e-09  9.91e-08
x2            -0.0049      0.003     -1.715      0.087        -0.010     0.001
==============================================================================
Omnibus:                       49.519   Durbin-Watson:                   1.965
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               61.372
Skew:                           0.668   Prob(JB):                     4.71e-14
Kurtosis:                       3.728   Cond. No.                     2.32e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.32e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

'''