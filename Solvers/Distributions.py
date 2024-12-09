#Discrete distributions
## Poisson distribution
import math

import numpy as np

lam = 2.5
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