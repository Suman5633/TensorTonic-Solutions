import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.array(X, dtype=float)

    # Number of samples
    n = X.shape[0]

    # Calculate mean of each feature
    mean = np.mean(X, axis=0)

    # Center the data
    X_centered = X - mean

    # Calculate sample covariance matrix
    covariance = (X_centered.T @ X_centered) / (n - 1)

    # Calculate sample standard deviation
    std = np.std(X, axis=0, ddof=1)

    # Calculate outer product of standard deviations
    denominator = np.outer(std, std)

    # Calculate correlation matrix
    result = np.full(covariance.shape, np.nan)

    np.divide(
        covariance,
        denominator,
        out=result,
        where=denominator != 0
    )

    return result
    pass