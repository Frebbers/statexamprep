import numpy as np
import scipy.stats as stats
import statsmodels.formula.api as smf
x = np.array([50, 100, 150, 200, 250, 300, 350, 400, 450, 500])
y = np.array([2.33, 4.21, 6.01, 7.51, 8.46, 8.93, 9.45, 10.70, 10.55, 10.74])
# Fit the linear regression model on y and x

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

# Method 2: Using statsmodels
# Fit the linear regression model
model = smf.ols('y ~ x', data={'x': x, 'y': y}).fit()
print(model.summary())


def calculate_confidence_intervals(x, y, confidence_level):
    # Fit the linear regression model
    model = smf.ols('y ~ x', data={'x': x, 'y': y}).fit()

    # Calculate the confidence intervals
    conf_intervals = model.conf_int(alpha=1-confidence_level)

    # Extract the confidence intervals for the slope and intercept
    intercept_conf_interval = conf_intervals.loc['Intercept']
    slope_conf_interval = conf_intervals.loc['x']

    return intercept_conf_interval, slope_conf_interval

if __name__ == "__main__":
    confidence_level = 0.99
    intercept_conf_interval, slope_conf_interval = calculate_confidence_intervals(x, y, confidence_level)

    print(f"{confidence_level*100}% Confidence Intervals:")
    print(f"Intercept: {intercept_conf_interval[0]:.4f} - {intercept_conf_interval[1]:.4f}")
    print(f"Slope: {slope_conf_interval[0]:.4f} - {slope_conf_interval[1]:.4f}")



