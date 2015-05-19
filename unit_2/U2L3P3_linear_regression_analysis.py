# Linear Regression Analysis
# https://courses.thinkful.com/data-001v2/project/2.3.3
# Challenge: follow along with the example

# 5.18 - Revised to follow SF's 3_LinearRegression_pandas_formula.py

from matplotlib import pyplot as plt
import lending_club_utils as utils
import pandas as pd
import statsmodels.formula.api as smf

# load and scrub
loans_data = utils.fetch_data_frame()
utils.add_FICO_score(loans_data)
utils.scrub_interest_rate(loans_data)

# Calculate our model
data = {'interest_rate':loans_data['Interest.Rate'],
        'fico': loans_data['FICO.Score']}

df = pd.DataFrame(data)


# Plot the data: shows a relationship of low FICO -> high interest rate
plt.plot(df["fico"], df["interest_rate"], 's', label="Interest Rate Awarded")
plt.xlabel("FICO score")
plt.ylabel("Interest Rate")
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()


# Ordinary Least Squares = Linear Regression
model = smf.ols(formula="interest_rate ~ fico", data=df)
fitted_model = model.fit()
coeffs = fitted_model.params
print fitted_model.summary()
print "The model obtained is y = {0} + {1}*x".format(*coeffs)
print coeffs
