import numpy as np
from scipy.stats import chi2_contingency

def chi_square_test(data):
    """
    Perform a Chi-Square test for independence.

    Parameters:
    - data: 2D array (contingency table with observed frequencies)

    Returns:
    - chi2_stat: Chi-Square statistic
    - p_value: p-value of the test
    - dof: Degrees of freedom
    - expected: Expected frequencies
    """
    chi2_stat, p_value, dof, expected = chi2_contingency(data)
    return chi2_stat, p_value, dof, expected

if __name__ == "__main__":
    # Contingency table for age groups and gender
    # Rows: [18-24, 25-29, 30-39]
    # Columns: [Males, Females]
    observed = np.array([
        [14048, 14128],  # 18-24
        [8215, 6028],    # 25-29
        [2735, 1397]     # 30-39
    ])

    # Perform the Chi-Square test
    chi2_stat, p_value, dof, expected = chi_square_test(observed)

    print(f"Chi-Square Statistic: {chi2_stat:.4f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Degrees of Freedom: {dof}")
    print(f"Expected Frequencies: \n{expected}")

    # Conclusion
    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis: There is a significant difference in proportions.")
    else:
        print("Fail to reject the null hypothesis: No significant difference in proportions.")
