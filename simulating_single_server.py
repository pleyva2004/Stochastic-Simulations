import math
from dataclasses import dataclass
import numpy as np

@dataclass
class Cust:
    arrival: float
    deadline: float

def simulate_one(T=100.0, lam=5.0, mu=4.0, patience_max=5.0, rng=None):
    if rng is None:
        rng = np.random.default_rng()
        
    t = 0.0
    # Server status
    busy = False
    # FIFO queue of customers waiting (not in service), store (arrival, deadline)
    Q = []
    lost = 0
    
    # next arrival time
    A = t + rng.exponential(1.0/lam)
    # next service completion time
    C = math.inf
    
    while True:
        # earliest abandonment among those waiting
        if Q:
            Dmin = min(c.deadline for c in Q)
        else:
            Dmin = math.inf
        
        # choose next event time
        tau = min(A, C, Dmin)
        if tau > T:
            break
        # advance time
        t = tau
        
        # Event priority: abandonment first, then completion, then arrival
        # Handle floating comparisons robustly
        eps = 1e-12
        if Dmin <= A + eps and Dmin <= C + eps:
            # Abandonment: remove the customer with earliest deadline
            # If there are multiple with same earliest deadline, remove one (any)
            min_dead = Dmin
            # Find first index with that deadline (tie-break doesn't matter)
            idx = None
            for i, c in enumerate(Q):
                if abs(c.deadline - min_dead) <= eps:
                    idx = i
                    break
            if idx is not None:
                Q.pop(idx)
                lost += 1
            # server state unchanged
            
        elif C <= A + eps and C <= Dmin + eps:
            # Service completion
            if not Q:
                busy = False
                C = math.inf
            else:
                # drop any who already expired by now (deadline <= t)
                while Q and Q[0].deadline <= t + eps:
                    Q.pop(0)
                    lost += 1
                if not Q:
                    busy = False
                    C = math.inf
                else:
                    # next still-waiting head starts service
                    Q.pop(0)
                    busy = True
                    C = t + rng.exponential(1.0/mu)
        else:
            # Arrival
            # schedule next arrival
            A = t + rng.exponential(1.0/lam)
            # new customer
            patience = rng.uniform(0.0, patience_max)
            deadline = t + patience
            if not busy and not Q:
                # starts service immediately
                busy = True
                C = t + rng.exponential(1.0/mu)
            else:
                # joins queue
                Q.append(Cust(arrival=t, deadline=deadline))
    
    return lost

# Run many replications
R = 500
rng = np.random.default_rng(42)
losses = np.array([simulate_one(rng=rng) for _ in range(R)], dtype=float)
mean_loss = losses.mean()
std_loss = losses.std(ddof=1)
ci_halfwidth = 1.96 * std_loss / math.sqrt(R)

mean_loss, std_loss, ci_halfwidth, losses[:10]

print(f"Expected number of lost customers by time T=100: {mean_loss:.4f} (± {ci_halfwidth:.4f})")