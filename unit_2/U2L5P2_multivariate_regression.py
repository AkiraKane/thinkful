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

# Mimicking the approach in "Multiple Regression using Statsmodels" at
# http://nbviewer.ipython.org/urls/s3.amazonaws.com/datarobotblog/notebooks/multiple_regression_in_python.ipynb#appendix

import lending_club_utils as utils
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf # This is different #

loan_data = utils.fetch_large_dataset()
# Fields

income = loan_data['annual_inc']

#scrubbed to a decimal
interest = loan_data['int_rate']

# scrubbed: 1 = 'RENT', 2='MORTGAGE', 3='OWNS'
owns = loan_data['owns']


# With two variables:
# int_rate  = b + m (annual_inc)
model = smf.ols(formula="interest ~ income", data=loan_data)
fitted_model = model.fit()
coeffs = fitted_model.params
print fitted_model.summary()
print "\n\nThe model obtained is y = {0} + {1}*x1".format(*coeffs)
print coeffs
print '\n\n\n'

# This graph doesn't show a clear trend between income and interest rate
# There aren't many loans for incomes
plt.scatter(loan_data.annual_inc, loan_data.int_rate, s=10, alpha=0.3)
plt.xlabel("income")
plt.ylabel("interest rate")
plt.show()



# Three variables: int_rate  = b + m (annual_inc) + n(home_ownership)

model = smf.ols(formula="interest ~ income + owns", data=loan_data)
fitted_model = model.fit()
coeffs = fitted_model.params
print fitted_model.summary()
print "\n\nThe model obtained is y = {0} + {1}*income + {2}*owns".format(*coeffs)
print coeffs


# Plot the data. What type is it? What should we expect from it?
# From SF's multivariate example:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(loan_data['annual_inc'], loan_data['owns'],  loan_data['int_rate'], "y measured")
ax.set_xlabel('annual_inc')
ax.set_ylabel('owns')
ax.set_zlabel('int_rate')
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()


# Still doesn't show a clear relationship.
# There are a few unusually high incomes that make the graph harder to read
# 29 loan applicants ( ~.01%) are millionaires

'''
In [6]: df['annual_inc'].describe()
Out[6]:
count     235629.000000
mean       74854.148281
std        55547.533374
min         3000.000000
25%        45377.000000
50%        65000.000000
75%        90000.000000
max      7500000.000000
Name: annual_inc, dtype: float64
'''

'''
In [7]: non_millionaires = df['annual_inc'].where(df['annual_inc'] < 1000000)

In [8]: non_millionaires.describe()
Out[8]:
count    235600.000000
mean      74624.052887
std       47682.688837
min        3000.000000
25%       45360.000000
50%       65000.000000
75%       90000.000000
max      999999.000000
Name: annual_inc, dtype: float64

'''

'''
# Curious - does the interest rate go up with the size of the loan?
# No clear relationship - there's a wide variety
plt.scatter(loan_data.funded_amnt, loan_data.int_rate, s=10, alpha=0.3)
plt.xlabel("funded")
plt.ylabel("interest rate")
plt.show()
'''

