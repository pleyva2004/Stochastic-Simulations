import numpy as np

def rolls_until_all_sums_rng(rng):
    seen = 0  # bitmask for sums 2..12 (11 sums) -> use bits 0..10
    target = (1 << 11) - 1
    rolls = 0
    while seen != target:
        # roll two fair dice
        s = rng.integers(1, 7) + rng.integers(1, 7)  # 2..12
        seen |= 1 << (s - 2)
        rolls += 1
    return rolls

def simulate(n_trials=20000, seed=42):
    rng = np.random.default_rng(seed)
    samples = np.fromiter((rolls_until_all_sums_rng(rng) for _ in range(n_trials)),
                          dtype=np.int32, count=n_trials)
    mean = samples.mean()
    return mean

mean = simulate()
print(mean)
