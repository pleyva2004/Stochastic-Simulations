import random
import math

def generate_geometric_comp():
    U1 = random.uniform(0, 1)
    if U1 < 0.5:
        p = 0.5  
    else:
        p = 1/3  

    U2 = random.uniform(0, 1)
    X = int(math.floor(math.log(U2) / math.log(1 - p))) + 1
    return X


if __name__ == "__main__":
    for _ in range(10):
        print(generate_geometric_comp())