import random


def simulate_exceed_prob(num_trials=20000, n_policies=1000, claim_prob=0.05, exp_mean=800.0, threshold=50000.0, seed=448):
    random.seed(seed)
    rate = 1.0 / exp_mean
    exceed = 0

    for _ in range(num_trials):
        n_claims = sum(random.random() < claim_prob for _ in range(n_policies))

        total = sum(random.expovariate(rate) for _ in range(n_claims))

        if total > threshold:
            exceed += 1

    return exceed / num_trials


if __name__ == "__main__":
    prob_estimate = simulate_exceed_prob(num_trials=20000)
    print(f"Estimated probability: {prob_estimate:.4f}")