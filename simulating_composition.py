import random
import math


def simulate_composition():

    U1 = random.uniform(0, 1)
    U2 = random.uniform(0, 1)

    if U1 < 0.3:
        X = math.floor(U2 * 5) + 1
    else:
        Y = math.floor(U2 * 70) + 1

        if Y < 16:
            X = 6
        elif Y < 29:
            X = 7
        elif Y < 42:
            X = 8
        elif Y < 58:
            X = 9
        else:
            X = 10
    
    return X

if __name__ == "__main__":
    for _ in range(10):
        print(simulate_composition())


