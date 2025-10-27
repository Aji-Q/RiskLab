import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf


def show_portfolio_risk_dashboard():
    st.header("Portfolio Risk Simulator")
    st.write("Build a portfolio and explore its risk metrics.")

    tickers_input = st.text_input("Enter tickers (comma separated)", "SPY,AAPL,BTC-USD")
    if not tickers_input:
        st.write("Please enter at least one ticker.")
        return

    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]
    window = st.slider("Lookback Window (days)", min_value=30, max_value=365, value=180)

    # Download price data
    data = yf.download(tickers, period=f"{window}d")["Adj Close"]
    returns = data.pct_change().dropna()

    if returns.empty:
        st.write("Not enough data to compute risk metrics.")
        return

    # Mean returns and covariance
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    # Global Minimum Variance Portfolio weights
    try:
        inv_cov = np.linalg.inv(cov_matrix.values)
        ones = np.ones(len(mean_returns))
        weights = inv_cov.dot(ones) / (ones.T.dot(inv_cov).dot(ones))
        weights_series = pd.Series(weights, index=mean_returns.index)
    except np.linalg.LinAlgError:
        st.write("Covariance matrix is singular, cannot compute optimal weights.")
        weights_series = pd.Series([1/len(mean_returns)]*len(mean_returns), index=mean_returns.index)

    # Portfolio expected return and volatility
    port_return = np.dot(weights_series, mean_returns)
    port_vol = np.sqrt(np.dot(weights_series.T, np.dot(cov_matrix, weights_series)))

    st.subheader("Global Minimum Variance Portfolio Weights")
    st.write(weights_series)

    st.subheader("Portfolio Metrics (daily)")
    st.write(f"Expected return: {port_return:.2%}")
    st.write(f"Volatility: {port_vol:.2%}")

    # Value at Risk for portfolio returns
    confidence_level = st.slider("VaR Confidence Level", min_value=0.90, max_value=0.99, value=0.95, step=0.01)
    portfolio_returns = returns.dot(weights_series)
    VaR = portfolio_returns.quantile(1 - confidence_level)
    st.write(f"{int(confidence_level*100)}% Historical VaR: {VaR:.2%}")

    st.subheader("Asset Correlation Matrix")
    st.write(returns.corr())

    st.subheader("Price Series")
    st.line_chart(data)
