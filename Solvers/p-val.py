from scipy.stats import t


def compute_p_value(sample_mean, null_mean, std_dev, sample_size):
    """
    Compute the p-value for a two-sided t-test.

    Parameters:
    - sample_mean: Observed sample mean
    - null_mean: Mean under the null hypothesis
    - std_dev: Sample standard deviation
    - sample_size: Number of observations

    Returns:
    - p-value for the two-sided test
    """
    # Compute the t-statistic
    t_stat = (sample_mean - null_mean) / (std_dev / (sample_size ** 0.5))

    # Degrees of freedom
    df = sample_size - 1

    # Compute the two-tailed p-value
    p_value = 2 * (1 - t.cdf(abs(t_stat), df))
    return t_stat, p_value


if __name__ == "__main__":
    # Given values
    sample_mean = 34.66
    null_mean = 30
    std_dev = 10.12
    sample_size = 40

    # Compute the p-value
    t_statistic, p_value = compute_p_value(sample_mean, null_mean, std_dev, sample_size)
    print(f"T-statistic: {t_statistic:.4f}")
    print(f"P-value: {p_value * 100:.2f}%")
