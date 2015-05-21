# -*- coding: UTF-8 -*-
# Logistic Regression Analysis
# https://courses.thinkful.com/data-001v2/project/2.4.3

import lending_club_utils as utils
import pandas as pd
import statsmodels.formula.api as smf

def extract_data(loans_data):
    data = {'fico': loans_data['FICO.Score'], 'interest': loans_data['Interest.Rate'],
            'discrete_rate':loans_data['Interest.below12']}
    df = pd.DataFrame(data)
    return df

def generate_model(df):
    '''
    Create a logistic regression model from loans data based on fields
    FICO.score, Interest.Rate, and Interest.below12
    :param df: a dataframe with fields for the independent vars fico and interest
    and the dependent var discrete_rate
    :return: a fitted logistic model
    '''
    model = smf.logit(formula='discrete_rate  ~ fico + interest', data=df)
    fitted_model = model.fit()
    return fitted_model


def calculate_probability(credit_score, loan_amount, fitted):
    '''
    Given our model, predict whether a candidate will qualify for a loan
    :param credit_score: a FICO score
    :param loan_amount:  amount of loan requested
    :param logit: our logistic regression model
    :return: a probability
    '''

    coeff = fitted.params.values
    print coeff
    return True

def loan_granted(credit_score, loan_amount, logit):
    granted = True if calculate_probability(credit_score,loan_amount,logit) else False
    return 'was' if granted else 'was NOT'

# ---- MAIN ----------
# load and scrub
loans_data = utils.fetch_and_prep_data_frame()
model_data = extract_data(loans_data)


#logit = generate_model(model_data)
#print logit.summary()


'''
template = 'Loan %s granted for FICO score %d and loan amount %d'

# The values the problem proposed:
credit_score = 720
loan_amount = 10000
print template % (loan_granted(credit_score, loan_amount, logit), credit_score, loan_amount)

# JR: these results look bogus
# Plug in some 'bad' values - you'd think these would be rejected, but no
'''
'''
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
colors = ['r' if bool(ib12) else 'b' for ib12 in loans_data['Interest.below12'] ]
ax.scatter(loans_data['FICO.Score'], loans_data['Amount.Requested'],  loans_data['Interest.below12'],
           c=colors)
ax.set_xlabel('FICO SCORE')
ax.set_ylabel('Amount.Requested')
ax.set_zlabel('InterestBelow12')
plt.show()
'''