#Discrete distributions
## Poisson distribution
import math

import numpy as np
from scipy.stats import binom

lam = 0.45 # the average number of events in a given interval
x = 5 # the number of events we are interested in seeing

#The probability of seeing exactly x events in a given interval
prob = (np.exp(-lam) * lam**x) / math.factorial(x)
print("The probability of seeing exactly x events in a given interval " + str(prob))

#The probability of seeing less than x events in a given interval
prob = sum([(np.exp(-lam) * lam**i) / math.factorial(i) for i in range(x)])
print("The probability of seeing less than x events in a given interval " + str(prob))

#the probability of seeing x or more events in a given interval
prob2 = 1-prob
print("The probability of seeing x or more events in a given interval " + str(prob2))

## Binomial distribution
n = 190  # the number of trials
p = 0.45  # the probability of success
k = 100  # the number of successes we are interested in seeing

#The probability of seeing exactly x successes in n trials
prob3 = binom.pmf(k, n, p)
print("The probability of seeing exactly x successes in n trials " + str(prob3))

#The probability of seeing more than x successes in n trials
prob4 = 1 - binom.cdf(k - 1, n, p)
print("The probability of seeing more than x successes in n trials " + str(prob4))