import numpy as np

rng = np.random.default_rng(448)  # reproducible

p = 0.2
n_contestants = 100

def simulate_expected_rounds(num_reps: int, chunk: int = 50000):
    samples = []
    remaining = num_reps
    while remaining > 0:
        k = min(chunk, remaining)
        # draw geometric(p) for a k x n_contestants matrix, take row-wise maxima
        geom = rng.geometric(p, size=(k, n_contestants))
        mx = geom.max(axis=1)
        samples.append(mx.astype(np.int32))
        remaining -= k
    m = np.concatenate(samples)
    return m

num_reps = 300_000  
max_rounds = simulate_expected_rounds(num_reps)

mean_est = max_rounds.mean()
print(mean_est)