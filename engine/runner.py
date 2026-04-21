# engine/runner.py

import numpy as np

def run_model(inputs, iwr):

    np.random.seed(42)

    # -----------------------------
    # SETUP
    # -----------------------------
    sims = 10000
    years = int(inputs["life_expectancy"] - inputs["retirement_age"])

    initial_portfolio = (
        inputs["tsp_balance"]
        + inputs["roth_balance"]
        + inputs["taxable_balance"]
    )

    mu = 0.05
    sigma = 0.15

    # -----------------------------
    # STORAGE
    # -----------------------------
    terminal_values = np.zeros(sims)

    # -----------------------------
    # MONTE CARLO LOOP
    # -----------------------------
    for s in range(sims):

        balance = initial_portfolio

        withdrawal = iwr * balance  # Year 1 withdrawal

        for t in range(years):

            # -----------------------------
            # APPLY WITHDRAWAL FIRST
            # -----------------------------
            balance -= withdrawal

            # Prevent negative portfolio
            if balance <= 0:
                balance = 0
                break

            # -----------------------------
            # APPLY MARKET RETURN
            # -----------------------------
            z = np.random.standard_t(df=5)
            annual_return = mu + sigma * z

            balance *= (1 + annual_return)

            # -----------------------------
            # UPDATE WITHDRAWAL (inflation proxy)
            # -----------------------------
            withdrawal *= 1.02  # simple inflation assumption

        terminal_values[s] = balance

    # -----------------------------
    # OUTPUT METRICS
    # -----------------------------
    median_terminal = np.median(terminal_values)
    p10_terminal = np.percentile(terminal_values, 10)

    return {
        "terminal": median_terminal,
        "p10": p10_terminal
    }