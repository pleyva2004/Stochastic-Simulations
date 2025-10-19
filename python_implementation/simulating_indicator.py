import random
import numpy as np

def simulate_hits(n=100, trials=100000):
    hits = []
    for _ in range(trials):
        deck = list(range(1, n+1))
        random.shuffle(deck)
        count = sum(1 for i, card in enumerate(deck, start=1) if card == i)
        hits.append(count)
    return np.mean(hits), np.var(hits, ddof=0)

mean, var = simulate_hits()
print("Estimated Expectation:", mean)
print("Estimated Variance:", var)
