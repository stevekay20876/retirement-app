from engine.monte_carlo import simulate_returns
from engine.withdrawals import compute_withdrawal

def run_model(inputs, iwr):
    years = int(inputs["life_expectancy"] - inputs["retirement_age"])
    paths = simulate_returns(inputs["tsp_balance"], years=years)

    terminal_values = paths[:, -1]
    median_terminal = terminal_values.mean()

    return {
        "terminal": median_terminal
    }
