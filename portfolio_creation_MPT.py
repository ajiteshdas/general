import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import datetime
import scipy.optimize as sco
import pandas_datareader.data as web

#stocks = ['ABC','CDE','DEF']

#Step1: download historical data
start_date = '01/01/2000'
end_date = '11/30/2019'

#Step2: Choose Adj Close for greater accuracy
data = web.DataReader(stocks, data_source='yahoo', start=start_date, end=end_date)['Adj Close']

#Step3: calculate daily returns
returns = np.log(data/data.shift(1))
returns

#Step4: Mean of daily returns of each stock
ri = returns.mean()
#Step4a: Annualized Mean daily returns of each stock
ri = (ri+1)**252 - 1
ri

#Step5: calculating the sigma(or covariance) matrix
cov_matrix = returns.cov()
cov_matrix

#Optional Step: calculating the SD matrix
var = returns.var()
daily_sd = np.sqrt(variances)
annual_sd = daily_sd * np.sqrt(252)

#Optional step: calculate the correlation matrix
corr_matrix = returns.corr()

#Step6: randomize weights, wi
wi = np.random.random(len(stocks)) #stock weights
#wi = np.array([.75, .25])
#wi /= np.sum(wi) #to ensure they sum upto 100%


#Step7a: Calculate portfolio return
p_return = np.dot(wi.T,ri)


#Step7a: Calculate portfolio variance
p_var = np.dot(wi.T,np.dot(cov_matrix,wi))

#portfolio creation using Monte Carlo simulation, change the num_portfolios to set the number of simulations
p_ret = []
p_vol = []
p_weights = []
p_sharpe = []

num_portfolios = 1000

for portfolio in range(num_portfolios):
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)
    p_weights.append(weights)
    returns = np.dot(weights.T, ri)
    p_ret.append(returns)
    var = np.dot(weights.T,np.dot(cov_matrix,weights))
    sd = np.sqrt(var)
    ann_sd = sd * np.sqrt(250)
    p_vol.append(ann_sd)

p_data = {'Returns': p_ret, 'Volatility':p_vol}

for counter, symbol in enumerate(data.columns.tolist()):
    p_data[symbol+' weight'] = [w[counter] for w in p_weights]

portfolios = pd.DataFrame(p_data)
portfolios

#Calculate Sharpe ratio
rf = 5.15% #91-tbill rate(riskfree rate)
portfolios['Sharpe'] = (portfolios['Returns'] - rf)/p_data['Volatility']

#get the porfolio with max Sharpe ratio
portfolios.iloc[portfolios['Sharpe'].idxmax()]

#plot portfolios to get Markowitz bullet
portfolios.plot.scatter(x='Volatility', y='Returns', grid=True)




