import numpy as np

def simulate_inflation(years, sims):
    inflation = np.random.normal(0.03, 0.01, (sims, years))
    return inflation
