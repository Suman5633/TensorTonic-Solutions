import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x_arr = np.array(x)
    y_arr = np.array(y)
    distance = np.sum(np.abs(x_arr - y_arr))
    return float(distance)
    pass