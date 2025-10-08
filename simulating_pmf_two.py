import math
import random

def simulate_pmf_two(alpha, beta):

    U1 = random.uniform(0, 1)

    X = ((-math.log(U1)) / alpha) ** (1/beta)
    
    return X

if __name__ == "__main__":
    alpha = 2
    beta = 3
    for _ in range(10):
        print(simulate_pmf_two(alpha, beta))