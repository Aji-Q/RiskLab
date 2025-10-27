import streamlit as st
from modules.market_risk import show_market_risk_dashboard
from modules.credit_risk import show_credit_risk_dashboard
from modules.portfolio_risk import show_portfolio_risk_dashboard

st.set_page_config(page_title="RiskLab", layout="wide")

st.title("RiskLab: Interactive FinTech Risk Playground")

module = st.sidebar.selectbox(
    "Select Module",
    ["Market Risk", "Credit Risk", "Portfolio Risk"]
)

if module == "Market Risk":
    show_market_risk_dashboard()
elif module == "Credit Risk":
    show_credit_risk_dashboard()
elif module == "Portfolio Risk":
    show_portfolio_risk_dashboard()
