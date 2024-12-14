import numpy as np
import scipy.stats as stats
from scipy.stats import norm
import math
#confidence_level = 0.975 #95% confidence level
confidence_level = 0.99 #99% confidence level
n = 40
sample_mean = 34.66 #use average here if given instead of mean
s = 10.12 #standard deviation
SEM = s / np.sqrt(n)
mu_lower = sample_mean - stats.t.ppf(confidence_level, df=n - 1) * SEM
mu_upper = sample_mean + stats.t.ppf(confidence_level, df=n - 1) * SEM
print(str(confidence_level) + " confidence interval for mean estimate: " + str(mu_lower), str(mu_upper))

# 95% confidence interval for standard deviation estimate
s_lower = s * np.sqrt(n / stats.chi2.ppf(confidence_level, df=n - 1))
s_upper = s * np.sqrt(n / stats.chi2.ppf(1-confidence_level, df=n - 1))
print ("95% confidence interval for the standard deviation estimate: " + str(s_lower), str(s_upper))

# confidence interval for mean estimate Method 3.9
significance = 0.1
n = 85
mean = 20/n
ci_lower = mean - stats.t.ppf(1-significance/2, df=n-1) * np.sqrt(mean*(1-mean)/n)
ci_upper = mean + stats.t.ppf(1-significance/2, df=n-1) * np.sqrt(mean*(1-mean)/n)
print("90% confidence interval for estimate: " + str(ci_lower), str(ci_upper))


from scipy.stats import norm
import math

def calculate_confidence_interval(
        mean_cheap: float,
        mean_expensive: float,
        std_dev_cheap: float,
        std_dev_expensive: float,
        n_cheap: int,
        n_expensive: int,
        confidence_level: float = 0.95
) -> (float, float):
    """
    Calculate the 95% confidence interval for the difference in mean tensile strengths.

    Parameters:
        mean_cheap (float): Mean tensile strength for the cheap screws.
        mean_expensive (float): Mean tensile strength for the expensive screws.
        std_dev_cheap (float): Standard deviation for the cheap screws.
        std_dev_expensive (float): Standard deviation for the expensive screws.
        n_cheap (int): Sample size for the cheap screws.
        n_expensive (int): Sample size for the expensive screws.
        confidence_level (float): Confidence level for the interval (default is 0.95).

    Returns:
        (float, float): The lower and upper bounds of the confidence interval.
    """
    # Calculate the difference in means
    difference_in_means = mean_cheap - mean_expensive

    # Calculate the standard error
    standard_error = math.sqrt((std_dev_cheap**2 / n_cheap) + (std_dev_expensive**2 / n_expensive))

    # Calculate the z-critical value
    z_critical = norm.ppf(1 - (1 - confidence_level) / 2)

    # Calculate the margin of error
    margin_of_error = z_critical * standard_error

    # Calculate the confidence interval
    lower_bound = difference_in_means - margin_of_error
    upper_bound = difference_in_means + margin_of_error

    # Return rounded results
    return round(lower_bound, 2), round(upper_bound, 2)


# Example usage with the given data
confidence_interval = calculate_confidence_interval(
    mean_cheap=1250,
    mean_expensive=1300,
    std_dev_cheap=54.24,
    std_dev_expensive=28.54,
    n_cheap=25000,
    n_expensive=15000
)

def calculate_confidence_interval(
        mean_1: float,
        mean_2: float,
        std_dev_1: float,
        std_dev_2: float,
        n_1: int,
        n_2: int,
        confidence_level: float = 0.95
) -> (float, float):
    """
    Calculate the confidence interval for the difference in means of two independent samples.

    Parameters:
        mean_1 (float): Mean of the first sample.
        mean_2 (float): Mean of the second sample.
        std_dev_1 (float): Standard deviation of the first sample.
        std_dev_2 (float): Standard deviation of the second sample.
        n_1 (int): Sample size of the first sample.
        n_2 (int): Sample size of the second sample.
        confidence_level (float): Confidence level for the interval (default is 0.95).

    Returns:
        (float, float): The lower and upper bounds of the confidence interval.
    """
    # Calculate the difference in means
    difference_in_means = mean_1 - mean_2

    # Calculate the standard error
    standard_error = math.sqrt((std_dev_1**2 / n_1) + (std_dev_2**2 / n_2))

    # Calculate the z-critical value
    z_critical = norm.ppf(1 - (1 - confidence_level) / 2)

    # Calculate the margin of error
    margin_of_error = z_critical * standard_error

    # Calculate the confidence interval
    lower_bound = difference_in_means - margin_of_error
    upper_bound = difference_in_means + margin_of_error

    # Return rounded results
    return round(lower_bound, 2), round(upper_bound, 2)


# Example usage with the given data
confidence_interval = calculate_confidence_interval(
    mean_1=1250,
    mean_2=1300,
    std_dev_1=54.24,
    std_dev_2=28.54,
    n_1=25000,
    n_2=15000
)
print("confidence interval for difference in means" + confidence_interval)





