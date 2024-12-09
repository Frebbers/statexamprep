import numpy as np
##Variance in discrete random variables
probs = [0.17, 0.22, 0.28, 0, 0.33]
x = np.random.choice([0, 1, 2, 3, 4], p=probs, size=100000)
mean = 2.1
variance = np.var(x)
print(variance)