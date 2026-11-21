import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    arr = np.array(x, dtype=float)
    variance = np.var(arr, ddof=1)
    standard_deviation = np.sqrt(variance)
    return {
        "variance": float(variance),
        "standard_deviation": float(standard_deviation)
    }
    pass