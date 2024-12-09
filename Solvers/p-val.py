import scipy.stats as stats
n = 45
degf = n-1
median = -1.74
pval = 2*stats.t.cdf(median, df=degf)
print(pval)
#pvalue greater than 0.05, so we do not reject the null hypothesis
# (The hypothesis is likely true)