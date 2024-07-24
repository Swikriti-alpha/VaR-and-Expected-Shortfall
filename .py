# VaR-and-Expected-Shortfall
#How to calculate VaR and Expected Shortfall using python
#VaR and Expected Shortfall:

#VaR shows the worst losses expected out of holding a security over a given period of time, given a certain level of confidence.

#Expected Shortfall or Conditional VaR shows the amount/value of losses, conditional that losses is great than the losses at c percentile in the tail region of loss distribution. IT measures the amount of loss if it were in the tail region.

#Step-1
#Import libraries:
import math
import numpy as np
from scipy.stats import norm


#step-2 (input data for 3 stocks A,B and C)
x = np.matrix([[0.4203], [0.1539], [0.3568]])
mu = np.matrix([[60/10000], [20/10000], [20/10000]])
vol = np.matrix([[2/100], [3/100], [1/100]])
rho = np.matrix([[1, 0.5, 0.25], [0.5, 1, 0.6], [0.25,0.6,1]])
sigma= np.matrix([[4.0000e-004, 3.0000e-004, 5.0000e-005],
[3.0000e-004,9.0000e-004, 1.8000e-004],
[5.0000e-005,1.8000e-004,1.0000e-004]])

alpha = 0.99

#step-3 compute VaR and ES
VaR_x = -x.T * mu + norm.ppf(alpha) * math.sqrt(x.T*sigma*x)

#compute ES
ES_x = -x.T * mu + (math.sqrt(x.T*sigma*x)/(1-alpha) * norm.ppf(alpha))


#Step-4 output results
print('VaR_x', VaR_x)
print('ES_x ', ES_x)
