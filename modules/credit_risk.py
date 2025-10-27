import streamlit as st


def show_credit_risk_dashboard():
    st.header("Credit Risk Simulator")
    credit_score = st.slider("Credit Score", 300, 850, 650)
    debt_income_ratio = st.slider("Debt-to-Income Ratio", 0.0, 1.0, 0.3)
    loan_amount = st.number_input("Loan Amount", min_value=1000.0, max_value=1000000.0, value=10000.0, step=1000.0)
    interest_rate = st.slider("Interest Rate (%)", 0.0, 20.0, 5.0)

    # simple PD model: high default risk when credit_score low and debt ratio high
    pd = max(0.01, min(0.99, (1 - (credit_score - 300) / 550) * debt_income_ratio + interest_rate / 1000))

    st.subheader("Estimated Probability of Default")
    st.write(f"{pd:.2%}")
