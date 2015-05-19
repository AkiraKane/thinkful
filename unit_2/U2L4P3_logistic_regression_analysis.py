# -*- coding: UTF-8 -*-
# Logistic Regression Analysis
# https://courses.thinkful.com/data-001v2/project/2.4.3

import numpy as np
import math
import statsmodels.api as sm
import lending_club_utils as utils



def generate_model(loans_data):
    '''
    Create a logistic regression model from loans data based on fields FICO.score, Interest.Rate, and Interest.below12
    :param loans_data: a dataframe with loans data and required fields
    :return: a logistic model
    '''
    ind_vars = ['FICO.Score','Amount.Requested']
    logit = sm.Logit(loans_data['Interest.below12'], loans_data[ind_vars])
    # p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount))

    return logit


def calculate_probability(credit_score, loan_amount, logit):
    '''
    Given our model, predict whether a candidate will qualify for a loan
    :param credit_score: a FICO score
    :param loan_amount:  amount of loan requested
    :param logit: our logistic regression model
    :return: a probability
    '''
    fitted = logit.fit()
    coeff = fitted.params.values
    print coeff

    # JR: My coeff didn't match the example in U2L4P3 step 4 - no intercept given, just coefficients
    # Couldn't find any documentation
    y_intercept = 0

    credit_score_coefficient = coeff[0]
    loan_amount_coefficient = coeff[1]
    credit_score = float(credit_score)
    value = y_intercept +  (credit_score * credit_score_coefficient) + (loan_amount_coefficient * loan_amount)
    probability = 1 / (1 + math.exp(value))
    print "DEBUG: probability calculated at ", probability
    return probability

def loan_granted(credit_score, loan_amount, logit):
    granted =  True if calculate_probability(credit_score,loan_amount,logit) else False
    return  "was" if granted else "was NOT"

# ---- MAIN ----------
# load and scrub
loans_data = utils.fetch_and_prep_data_frame()
logit = generate_model(loans_data)

template = "Loan %s granted for FICO score %d and loan amount %d"

# The values the problem proposed:
credit_score = 720
loan_amount = 10000
print template % (loan_granted(credit_score, loan_amount, logit), credit_score, loan_amount)

# JR: these results look bogus
# Plug in some 'bad' values - you'd think these would be rejected, but no
credit_score = 400
loan_amount = 10000000
print template % (loan_granted(credit_score, loan_amount, logit), credit_score, loan_amount)


credit_score = 250
loan_amount = 100000000000
print template % (loan_granted(credit_score, loan_amount, logit), credit_score, loan_amount)


# SF says: Plot your data
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = ["r" if bool(ib12) else "b" for ib12 in loans_data['Interest.below12'] ]
ax.scatter(loans_data['FICO.Score'], loans_data['Amount.Requested'],  loans_data['Interest.below12'],
           c=colors)
ax.set_xlabel('FICO SCORE')
ax.set_ylabel('Amount.Requested')
ax.set_zlabel('InterestBelow12')
plt.show()