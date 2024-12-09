import numpy as np
import pandas as pd
#One-way ANOVA
y = np.array([253.7, 241.2, 255.8, 249.3, #location 1
              261.1, 244.2, 250.5, 264.9, 259.3, #location 2
              257.9, 263.5, 258.6, #location 3
              244.1, 244.9, 243.9, 247.1]) #location 4
treatm = pd.Categorical([1, 1, 1, 1,
                         2, 2, 2, 2, 2,
                         3, 3, 3,
                         4, 4, 4, 4])

D = pd.DataFrame({'y': y, 'treatm': treatm})
mu = np.mean(y)
#print(D.groupby('treatm',observed=True)['y'].var())
#Effect of location 1
effect1 = np.mean(D[D['treatm'] == 1]['y']) - mu
print("effect 1: " + str(effect1))
#Effect of location 2
effect2 = np.mean(D[D['treatm'] == 2]['y']) - mu
print("effect 2: " + str(effect2))
#Effect of location 3
effect3 = np.mean(D[D['treatm'] == 3]['y']) - mu
print("effect 3: " + str(effect3))
#Effect of location 4
effect4 = np.mean(D[D['treatm'] == 4]['y']) - mu
print("effect 4: " + str(effect4))


#Estimate error standard deviation
# Group means
group_means = D.groupby('treatm', observed=True)['y'].mean()

# Convert 'treatm' to numeric type for compatibility
D['treatm_numeric'] = D['treatm'].astype(int)

# Map group means to numeric treatments
D['group_mean'] = D['treatm_numeric'].apply(lambda t: group_means[t])

# Calculate residuals
D['residual'] = D['y'] - D['group_mean']

# Calculate residual sum of squares
SS_res = np.sum(D['residual']**2)

# Degrees of freedom for error
n_total = len(y)
n_groups = len(group_means)
df_error = n_total - n_groups

# Estimate of error standard deviation
error_std_dev = np.sqrt(SS_res / df_error)

print(f"Error standard deviation: {error_std_dev:.4f}")