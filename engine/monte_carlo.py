import numpy as np

def simulate_returns(balance, mu=0.05, sigma=0.15, years=30, sims=1000):
    paths = np.zeros((sims, years))
    paths[:, 0] = balance
    for t in range(1, years):
        z = np.random.standard_t(df=5, size=sims)
        paths[:, t] = paths[:, t-1] * (1 + mu + sigma * z)
    return paths
