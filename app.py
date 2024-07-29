import streamlit as st
from capm import CAPM
import pandas as pd
from datetime import datetime

st.title('CAPM Analysis Tool')

# User Inputs
stock = st.text_input('Enter Stock Ticker (e.g., HDFCBANK):', 'HDFCBANK')
indices = ['^NSEI (Nifty 50)', '^BSESN (Sensex)', '^GSPC (S&P 500)']
market_index = st.selectbox('Choose Market Index:', indices)

st.write("Select the date range for the stock data to calculate returns:")
start_date = st.date_input('Start Date:', value=datetime(2020, 1, 1).date())
end_date = st.date_input('End Date:', value=datetime(2024, 7, 20).date())

risk_free_rate = st.number_input('Risk-Free Interest Rate:', min_value=0.0, max_value=1.0, value=0.05, step=0.01)

# Display message for Indian stock
if market_index in ['^NSEI (Nifty 50)', '^BSESN (Sensex)']:
    st.write("Make sure you add '.NS' to the stock ticker for Indian stocks.")

# Format market index
market_index = market_index.split()[0]

# Initialize and run CAPM analysis
if st.button('Run Analysis'):
    capm = CAPM(stock, market_index, start_date, end_date, risk_free_rate)
    capm.initialize()
    beta = capm.calculate_beta()
    beta_reg, alpha_reg, expected_return = capm.regression()
    
    st.write(f"Calculated Beta: {beta:.4f}")
    st.write(f"Beta from Regression: {beta_reg:.4f}")
    st.write(f"Alpha from Regression: {alpha_reg:.4f}")
    st.write(f"Expected Annual Return: {expected_return:.4f}")
    
    fig, axis = capm.get_regression_plot(alpha_reg, beta_reg)
    st.pyplot(fig)  # Display the plot in Streamlit
