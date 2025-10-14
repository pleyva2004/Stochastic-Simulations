import random
import math

def sample_uniform():
    return random.random()  

def sample_exponential(lmbda=1.0):
    u = random.random()
    return -math.log(1 - u) / lmbda

def sample_normal(mu=0.0, sigma=1.0):
      
    u1 = random.random()
    u2 = random.random()
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return mu + sigma * z0

p = [0.5, 0.3, 0.2]

samplers = [sample_uniform, sample_exponential, sample_normal]

def sample_composition():
    
    u = random.random()
    cumulative = 0.0
    for i, pi in enumerate(p):
        cumulative += pi
        if u < cumulative:
            chosen_sampler = samplers[i]
            break

    return chosen_sampler()

samples = [sample_composition() for _ in range(10)]
print(samples)
