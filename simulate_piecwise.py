import numpy as np

def sample_X(n, seed=None):
    rng = np.random.default_rng(seed)
    samples = []
    for _ in range(n):
        # Step 1: pick odd or even group
        if rng.random() < 0.55:   # odd group
            k = rng.integers(0, 5)   # 0..4
            x = 5 + 2*k              # {5,7,9,11,13}
        else:                      # even group
            k = rng.integers(0, 5)
            x = 6 + 2*k              # {6,8,10,12,14}
        samples.append(x)
    return samples


