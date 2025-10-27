import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf


def show_portfolio_risk_dashboard():
    st.header("Portfolio Risk Simulator")
    st.write("Build a portfolio and explore its risk metrics.")
    tickers_input = st.text_input("Enter tickers (comma separated)", "AAPL,MSFT,GOOGL")
    if tickers_input:
        tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]
        num_assets = len(tickers)
        weights = []
        st.subheader("Set portfolio weights")
        for t in tickers:
            weight = st.number_input(f"Weight for {t}", min_value=0.0, max_value=1.0, value=1.0/num_assets, step=0.01)
            weights.append(weight)
        weights = np.array(weights)
        if abs(np.sum(weights) - 1.0) > 1e-3:
            st.warning("Weights do not sum to 1. Normalizing weights.")
            weights = weights / np.sum(weights)
        # Download price data
        data = yf.download(tickers, period="1y")["Adj Close"]
        returns = data.pct_change().dropna()
        mean_returns = returns.mean() * 252
        cov_matrix = returns.cov() * 252
        # Portfolio metrics
        portfolio_return = np.dot(mean_returns, weights)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        # Value at Risk (simple parametric)
        confidence_level = st.slider("VaR confidence level", 0.90, 0.99, 0.95)
        portfolio_returns = returns.dot(weights)
        VaR = np.percentile(portfolio_returns, (1 - confidence_level) * 100)
        st.subheader("Portfolio Metrics")
        st.metric("Expected annual return", f"{portfolio_return:.2%}")
        st.metric("Expected annual volatility", f"{portfolio_volatility:.2%}")
        st.metric(f"{int(confidence_level * 100)}% VaR (daily)", f"{VaR:.2%}")
        st.line_chart(data)
