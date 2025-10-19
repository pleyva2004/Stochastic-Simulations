import numpy as np
import math

def truncated_poisson_pmf(i, lam, k):
    numerator = math.exp(-lam) * (lam**i) / math.factorial(i)
    denominator = sum(math.exp(-lam) * (lam**j) / math.factorial(j) for j in range(k+1))
    return numerator / denominator


def sample_truncated_poisson_inverse(lam, k):
    probs = [truncated_poisson_pmf(i, lam, k) for i in range(k+1)]
    cdf = np.cumsum(probs)
    u = np.random.rand()
    return np.searchsorted(cdf, u)

def sample_truncated_poisson_accept(lam, k):
    while True:
        y = np.random.poisson(lam)
        if y <= k:
            return y

lam = 3.0
k = 6
n = 10000

samples_inverse = [sample_truncated_poisson_inverse(lam, k) for _ in range(n)]
samples_accept  = [sample_truncated_poisson_accept(lam, k) for _ in range(n)]

print("Mean (Inverse):", np.mean(samples_inverse))
print("Mean (Accept-Reject):", np.mean(samples_accept))
