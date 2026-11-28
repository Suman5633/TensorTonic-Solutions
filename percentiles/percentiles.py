import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
     # Step 1: Sort the data
    x = np.sort(np.array(x, dtype=float))

    # Step 2: Convert q into NumPy array
    q = np.array(q, dtype=float)

    # Step 3: Calculate percentile positions
    r = (q / 100) * (len(x) - 1)

    # Step 4: Find lower and upper indices
    l = np.floor(r).astype(int)
    u = np.ceil(r).astype(int)

    # Step 5: Calculate interpolation weight
    w = r - l

    # Step 6: Linear interpolation
    result = (1 - w) * x[l] + w * x[u]

    return result
    pass