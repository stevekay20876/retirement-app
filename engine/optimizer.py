from scipy.optimize import brentq
from engine.runner import run_model
import numpy as np

def find_iwr(inputs):

    def objective(iwr):
        np.random.seed(42)
        result = run_model(inputs, iwr)
        return result["terminal"] - inputs["estate_floor"]

    low = objective(0.01)
    high = objective(0.15)

    # --- CASE 1: No root exists ---
    if low > 0 and high > 0:
        # Portfolio always exceeds floor → return max IWR
        return 0.15

    if low < 0 and high < 0:
        # Portfolio always below floor → return minimum IWR
        return 0.01

    # --- CASE 2: Root exists ---
    return brentq(objective, 0.01, 0.15, xtol=1e-4, maxiter=15)