import random
import math

def simulate_pmf_three():
    U = random.uniform(0, 1)

    if U <= 0.5:
        X = 0.5 * math.log(2 * U)
    else:
        X = -0.5 * math.log(2 * (1 - U))

    return X

if __name__ == "__main__":
    for _ in range(10):
        print(simulate_pmf_three())