import numpy as np

def simulate_geometric_method(n=25, p=0.8, num_trials=100000):
    q = 1 - p
    uniforms_used = []

    for _ in range(num_trials):
        remaining = n
        count = 0
        while remaining > 0:
            # One uniform to simulate a geometric
            U = np.random.rand()
            count += 1
            # Geometric(q): ceil(log(U)/log(1-q))
            j = int(np.ceil(np.log(U) / np.log(1 - q)))
            if j >= remaining:
                break
            remaining -= j
        uniforms_used.append(count)

    return np.mean(uniforms_used)

mean = simulate_geometric_method()
print(mean)
