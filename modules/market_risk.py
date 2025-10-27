import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from scipy.stats import norm


def show_market_risk_dashboard():
    st.header("Market Risk Dashboard")
    tickers = st.multiselect("Select assets", options=["SPY", "AAPL", "BTC-USD"], default=["SPY"])
    window = st.slider("Lookback Window (days)", min_value=30, max_value=365, value=90)
    confidence_level = st.slider("VaR Confidence Level", min_value=0.90, max_value=0.99, value=0.95, step=0.01)
    method = st.selectbox("VaR Method", options=["Historical", "Variance-Covariance"])

    if not tickers:
        st.write("Please select at least one asset.")
        return

    data = yf.download(tickers, period=f"{window}d")["Adj Close"]
    returns = data.pct_change().dropna()

    if method == "Historical":
        var = returns.quantile(1 - confidence_level)
    else:
        mean_returns = returns.mean()
        std_returns = returns.std()
        z_score = norm.ppf(confidence_level)
        var = mean_returns - z_score * std_returns

    st.subheader(f"{method} VaR")
    st.write(var)
    st.subheader("Price Time Series")
    st.line_chart(data)
