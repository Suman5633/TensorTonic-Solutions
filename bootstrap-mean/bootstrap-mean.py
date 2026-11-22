import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    rng = np.random.default_rng(seed)

    x = np.array(x, dtype=float)

    n = len(x)

    # Generate bootstrap samples with replacement
    samples = rng.choice(
        x,
        size=(n_bootstrap, n),
        replace=True
    )

    # Calculate mean of each bootstrap sample
    means = np.mean(samples, axis=1)

    # Calculate bootstrap mean
    boot_mean = np.mean(means)

    # Calculate confidence interval
    alpha = (1 - ci) / 2

    lower = np.quantile(means, alpha)
    upper = np.quantile(means, 1 - alpha)

    return {
        "bootstrap_mean": float(boot_mean),
        "lower": float(lower),
        "upper": float(upper)
    }
    pass