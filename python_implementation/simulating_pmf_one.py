import random
import math

def simulate_pmf_one():
    U1 = random.uniform(0, 1)
    U2 = random.uniform(0, 1)

    if U1 <= 0.25:
        X = 2*math.sqrt(U2) + 2
    else:
        X = 6 - math.sqrt(12*(1 - U2))