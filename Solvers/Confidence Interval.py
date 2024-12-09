import numpy as np
import scipy.stats as stats
confidence_level = 0.975 #95% confidence level
n=30
mean = 1.01
s = 0.09 #standard deviation
SEM = s / np.sqrt(n)
mu_lower = mean - stats.t.ppf(confidence_level, df=n - 1) * SEM
mu_upper = mean + stats.t.ppf(confidence_level, df=n - 1) * SEM
print("95% confidence interval for mean estimate: " + str(mu_lower), str(mu_upper))
# 95% confidence interval for standard deviation estimate
s_lower = s * np.sqrt(n / stats.chi2.ppf(0.975, df=n - 1))
s_upper = s * np.sqrt(n / stats.chi2.ppf(0.025, df=n - 1))
print ("95% confidence interval for the standard deviation estimate: " + str(s_lower), str(s_upper))

# confidence interval for mean estimate Method 3.9
significance = 0.1
n = 85
mean = 20/n
ci_lower = mean - stats.t.ppf(1-significance/2, df=n-1) * np.sqrt(mean*(1-mean)/n)
ci_upper = mean + stats.t.ppf(1-significance/2, df=n-1) * np.sqrt(mean*(1-mean)/n)
print("90% confidence interval for estimate: " + str(ci_lower), str(ci_upper))

