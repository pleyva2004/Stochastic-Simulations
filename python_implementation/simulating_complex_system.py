# Simulation per the user's specification.
# NHPP arrivals with triangular 10-hour period between 4 and 19 per hour.
# Single server with Exp(25) service; server takes Uniform(0, 0.3) breaks whenever a service completes
# and finds no jobs waiting. If on return there's still no job, goes on another break.
# Goal: estimate expected time on break during first 100 hours. 500 replications.

import math
import random
import numpy as np

T_HORIZON = 100.0
LAMBDA_MAX = 19.0
SERVICE_RATE = 25.0  # per hour
BREAK_MAX = 0.3  # Uniform(0, 0.3) hours
N_RUNS = 500

rng = np.random.default_rng(448)  # reproducible

def lambda_t(t):
    # periodic triangular rate with period 10h: 4 -> 19 over 5h, then 19 -> 4 next 5h.
    phase = t % 10.0
    if phase < 5.0:
        return 4.0 + 3.0 * phase  # slope up
    else:
        return 34.0 - 3.0 * phase  # slope down

def generate_arrivals_thinning(T):
    arrivals = []
    t = 0.0
    while True:
        # homogeneous proposal at LAMBDA_MAX
        t += rng.exponential(1.0 / LAMBDA_MAX)
        if t > T:
            break
        if rng.random() < (lambda_t(t) / LAMBDA_MAX):
            arrivals.append(t)
    return arrivals

def simulate_one(T):
    arrivals = generate_arrivals_thinning(T)
    i_arr = 0
    next_arrival = arrivals[i_arr] if i_arr < len(arrivals) else None

    t = 0.0
    queue = 0
    server_busy = False
    on_break = False
    t_service_complete = None
    t_break_end = None

    break_time_accum = 0.0
    current_break_start = None

    def start_service(now):
        nonlocal server_busy, t_service_complete
        server_busy = True
        t_service_complete = now + rng.exponential(1.0 / SERVICE_RATE)

    def start_break(now):
        nonlocal on_break, t_break_end, current_break_start, break_time_accum
        on_break = True
        current_break_start = now
        duration = rng.uniform(0.0, BREAK_MAX)
        t_break_end = now + duration
        # will add to break_time_accum when break ends or at horizon cutoff

    while True:
        # Determine next event time
        candidates = []
        if next_arrival is not None:
            candidates.append(next_arrival)
        if t_service_complete is not None:
            candidates.append(t_service_complete)
        if t_break_end is not None:
            candidates.append(t_break_end)
        if not candidates:
            # No more events; if on break, add remaining time until T; otherwise we're idle
            if on_break and t < T:
                break_time_accum += min(T, T) - t  # add remaining
            break

        t_next = min(candidates)
        if t_next > T:
            # advance to T and finish
            if on_break and current_break_start is not None:
                # add partial break duration up to T
                break_time_accum += max(0.0, T - max(current_break_start, t))
            break

        # Advance time to next event
        t = t_next

        if next_arrival is not None and abs(t - next_arrival) < 1e-12:
            # Arrival event
            i_arr += 1
            next_arrival = arrivals[i_arr] if i_arr < len(arrivals) else None
            if server_busy or on_break:
                queue += 1
            else:
                # idle & available -> start service immediately
                start_service(t)

        elif t_service_complete is not None and abs(t - t_service_complete) < 1e-12:
            # Service completion
            server_busy = False
            t_service_complete = None
            if queue > 0:
                queue -= 1
                start_service(t)
            else:
                # go on break
                start_break(t)

        elif t_break_end is not None and abs(t - t_break_end) < 1e-12:
            # Break ends
            # Add this break duration to accumulator
            if current_break_start is not None:
                break_time_accum += t - current_break_start
            on_break = False
            t_break_end = None
            current_break_start = None
            if queue > 0:
                # start service
                start_service(t)
            else:
                # immediately start another break
                start_break(t)

        else:
            # Shouldn't happen
            pass

    return break_time_accum

break_times = np.array([simulate_one(T_HORIZON) for _ in range(N_RUNS)])

mean_break = break_times.mean()
std_break = break_times.std(ddof=1)
se_break = std_break / math.sqrt(N_RUNS)
ci_low = mean_break - 1.96 * se_break
ci_high = mean_break + 1.96 * se_break

mean_break, std_break, se_break, ci_low, ci_high
print(f" Expected time on break during first 100 hours: {mean_break:.4f} (± {se_break:.4f})")
