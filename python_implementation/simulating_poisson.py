import random
import math

def poisson_process_horizon(lmbda: float, T: float):

    t = 0.0
    arrivals =[]
    while t < T:
        U = random.random()              # Uniform(0,1)
        X = -math.log(U) / lmbda         # Exp(lmbda) interarrival (inverse-CDF)
        t += X
        arrivals.append(t)
    return arrivals

if __name__ == "__main__":
    times = poisson_process_horizon(lmbda=3.0, T=5.0)
    print(times)  
