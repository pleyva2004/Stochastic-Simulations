import random, math

def poisson_knuth(lmbda=5.0):
    L = math.exp(-lmbda)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1  

def estimate_mean_var_bus_arrivals(R=10000, lmbda=5.0):
    Ns = [poisson_knuth(lmbda) for _ in range(R)]
    meanN = sum(Ns) / R
    varN  = sum((x - meanN) ** 2 for x in Ns) / (R - 1)
    return meanN, varN

if __name__ == "__main__":
    meanN, varN = estimate_mean_var_bus_arrivals(R=20000, lmbda=5.0)
    print(f"Estimated E[N(1)] = {meanN:.3f}, Var[N(1)] = {varN:.3f}")
