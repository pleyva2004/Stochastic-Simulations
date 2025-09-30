import random

def sample_inverse():
    U = random.random()  # uniform(0,1)
    if U < 0.3:
        return 1
    elif U < 0.5:
        return 2
    elif U < 0.85:
        return 3
    else:
        return 4

# Example: generate 10 samples
print([sample_inverse() for _ in range(10)])
