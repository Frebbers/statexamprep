import numpy as np
x = np.array([0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 12, 12])
y = np.array([16, 116, 1170, 841, 2287, 2012, 2653, 3333, 4270, 3999, 5750, 5407])
#Fit the linear regression model on y and x

# Step 1: Calculate the means of x and y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Step 2: Calculate the deviations from the mean
x_dev = x - mean_x
y_dev = y - mean_y

# Step 3: Calculate the slope
slope = np.sum(x_dev * y_dev) / np.sum(x_dev**2)

# Step 4: Calculate the intercept
intercept = mean_y - slope * mean_x

print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
