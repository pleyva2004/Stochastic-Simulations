import random
import numpy as np

def simulate_n():

    sum_u = 0
    n_count = 0
    while sum_u <= 1:
        u = random.uniform(0, 1)
        sum_u += u
        n_count += 1
    return n_count

def main():
    run_counts = [100, 1000, 10000]

    for k in run_counts:
        n_values = [simulate_n() for _ in range(k)]
        average_n = sum(n_values) / k
        print(f"Estimate of E[N] with {k} simulations: {average_n}")




def simulate_n_2():

    product = 1
    n_count = 0
    e_minus_3 = np.exp(-3)

    
    while product >= e_minus_3:
        u = random.uniform(0, 1)
        product *= u
        n_count += 1
    return n_count - 1
    

def main_2():
    num_simulations = 100000

    n_values = [simulate_n_2() for _ in range(num_simulations)]

    e_n_estimate = np.mean(n_values)

    probabilities = {}
    for i in range(7):
        count = n_values.count(i)
        probabilities[i] = count / num_simulations
        
    print(f"a. Estimated E[N] by simulation (from {num_simulations} runs): {e_n_estimate:.4f}")
    print("\nb. Estimated P{N=i} for i=0, 1, 2, 3, 4, 5, 6 by simulation:")
    for i in range(7):
        print(f"P{{N={i}}} = {probabilities[i]:.4f}")
    

def simulate_n_3(k):

    total_1 = 0
    total_2 = 0
    total_3 = 0

    for i in range(k):
        u = random.uniform(0, 1)
        eU = np.exp(u)
        total_1 += eU*u

        total_2 += u

        total_3 += eU
    
    average_1 = total_1 / k
    average_2 = total_2 / k
    average_3 = total_3 / k

    return average_1 - average_2 * average_3


def main_3():
    k = 100000
    result = simulate_n_3(k)
    print(f"a. Estimated Cov(U, e^U) by simulation (from {k} runs): {result:.4f}")




if __name__ == "__main__":
    main_3()