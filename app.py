import streamlit as st
from engine.optimizer import find_iwr
from engine.runner import run_model

st.set_page_config(layout="wide")
st.title("Retirement Simulation Engine")

st.header("Inputs")

current_age = st.number_input("Current Age")
retirement_age = st.number_input("Retirement Age")
life_expectancy = st.number_input("Life Expectancy Age")
tsp_balance = st.number_input("TSP Balance")
roth_balance = st.number_input("Roth Balance")
taxable_balance = st.number_input("Taxable Balance")
estate_floor = st.number_input("Target Estate Floor")

if st.button("Run Simulation"):
    inputs = {
        "current_age": current_age,
        "retirement_age": retirement_age,
        "life_expectancy": life_expectancy,
        "tsp_balance": tsp_balance,
        "roth_balance": roth_balance,
        "taxable_balance": taxable_balance,
        "estate_floor": estate_floor
    }

    iwr = find_iwr(inputs)
    results = run_model(inputs, iwr)

    st.success(f"Optimal IWR: {iwr:.4%}")
    st.write(results)
