import streamlit as st
import math


def show_credit_risk_dashboard():
    st.header("Credit Risk Simulator")

    # Input parameters
    credit_score = st.slider("Credit Score", 300, 850, 650)
    debt_income_ratio = st.slider("Debt-to-Income Ratio", 0.0, 1.0, 0.3)
    loan_amount = st.number_input("Loan Amount", min_value=1000.0, max_value=1000000.0, value=10000.0, step=1000.0)
    interest_rate = st.slider("Interest Rate (%)", 0.0, 20.0, 5.0)

    # Logistic PD model: higher credit score lowers PD, higher debt ratio and interest rate increase PD
    intercept = -1.5
    coef_credit = -5.0 / 550  # Negative effect per point above 300
    coef_debt = 3.0
    coef_interest = 0.05

    x = intercept + coef_credit * (credit_score - 300) + coef_debt * debt_income_ratio + coef_interest * interest_rate
    pd = 1 / (1 + math.exp(-x))
    pd = max(0.001, min(0.999, pd))  # Bound PD between 0.1% and 99.9%

    # Loss Given Default (LGD) slider: proportion of exposure lost if default occurs
    lgd = st.slider("Loss Given Default (LGD)", 0.0, 1.0, 0.45)

    # Exposure at Default (EAD): assumed equal to loan_amount by default but adjustable
    ead = st.number_input("Exposure at Default (EAD)", min_value=0.0, max_value=loan_amount, value=loan_amount)

    expected_loss = pd * lgd * ead

    st.subheader("Estimated Probability of Default (PD)")
    st.write(f"{pd:.2%}")

    st.subheader("Expected Loss (EL)")
    st.write(f"${expected_loss:,.2f}")
