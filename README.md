# RiskLab  
  
RiskLab is an interactive FinTech risk playground built with Streamlit. It provides hands-on modules that teach financial risk concepts through interactive dashboards.  
  
## Features  
  
- Real-time market risk dashboard with VaR and CVaR calculations for selected assets.  
- Credit risk simulator allowing users to adjust borrower parameters and see the resulting default probability.  
- Portfolio risk simulator to construct multi-asset portfolios, compute expected return, volatility and Value at Risk.  
- Modular design: each module is encapsulated in its own file in the `modules` directory for clarity and extensibility.  
  
## Installation  
  
1. Clone the repository.  
2. Install the required dependencies using pip:  
  
```
pip install -r requirements.txt
```  
  
## Usage  
  
Run the Streamlit app from the project root:  
  
```
streamlit run app.py
```  
  
The app will open in your browser. Use the sidebar to navigate between modules and experiment with parameters to learn how different factors influence financial risk.  
  
## Project Structure  
  
- `app.py` – main entry point that sets up the Streamlit page and loads modules.  
- `modules/market_risk.py` – provides the market risk dashboard using historical price data from yfinance.  
- `modules/credit_risk.py` – implements a simple credit risk model where users can adjust credit score and other factors.  
- `modules/portfolio_risk.py` – allows building a portfolio of tickers, calculates expected return, volatility and VaR.  
- `requirements.txt` – lists Python packages needed to run the project.  
  
## Contributing  
  
Feel free to fork the repository and submit pull requests to enhance modules or add new ones like liquidity risk, stress testing, etc. Suggestions and improvements are welcome. 
