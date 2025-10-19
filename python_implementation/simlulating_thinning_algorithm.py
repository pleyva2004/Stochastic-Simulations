#Lewis–Shedler thinning
import math, random

def lam(t): 
        return 3.0 + 4.0/(t+1.0)

def nhpp_thinning(T=10.0):
  
    lam_star = 7.0  

    t = 0.0
    S = []

    while t < T:
        u1 = random.random()
        w = -math.log(u1)/lam_star
        t += w

        u2 = random.random()
        if u2 <= lam(t)/lam_star:
            S.append(t)
    return S

times = nhpp_thinning(T=10.0)
print(times)
