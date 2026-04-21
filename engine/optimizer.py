from scipy.optimize import brentq
from engine.runner import run_model
import numpy as np

def find_iwr(inputs):
    def objective(iwr):
        np.random.seed(42)
        result = run_model(inputs, iwr)
        return result["terminal"] - inputs["estate_floor"]
    return brentq(objective, 0.01, 0.15)
