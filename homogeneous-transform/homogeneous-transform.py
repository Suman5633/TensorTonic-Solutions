import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    # Write code here
    T = np.array(T, dtype=float)
    points = np.array(points, dtype=float)

    # Check whether input is a single point
    single_point = points.ndim == 1

    if single_point:
        points = points.reshape(1, 3)

    # Add homogeneous coordinate 1
    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack((points, ones))

    # Apply transformation
    transformed = points_h @ T.T

    # Return first three coordinates
    result = transformed[:, :3]

    if single_point:
        return result[0]

    return result
    pass