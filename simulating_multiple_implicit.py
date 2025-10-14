import random, math

def sample_uniform01():
    return random.random()

def sample_exponential(rate=2.0):
    u = random.random()
    return -math.log(1.0 - u) / rate

def choice_by_probs(ps):
    u, cum = random.random(), 0.0
    for i, p in enumerate(ps):
        cum += p
        if u < cum:
            return i
    return len(ps) - 1

def sample_a():
    ks = [1, 3, 5]
    i = choice_by_probs([1/3, 1/3, 1/3])
    U = sample_uniform01()
    return U ** (1.0 / ks[i])

def sample_b():
    comp = choice_by_probs([1/3, 1/3, 1/3])
    if comp in (0, 1):                
        return sample_uniform01()
    else:                              
        return sample_exponential(rate=2.0)

def sample_c(alphas):
    i = choice_by_probs(alphas)        
    U = sample_uniform01()
    power = i + 1                      
    return U ** (1.0 / power)

if __name__ == "__main__":
    print("a:", [sample_a() for _ in range(5)])
    print("b:", [sample_b() for _ in range(5)])
    print("c (alphas=[0.2,0.3,0.5]):", [sample_c([0.2,0.3,0.5]) for _ in range(5)])
