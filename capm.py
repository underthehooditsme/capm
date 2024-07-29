import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

MONTHS_IN_YEAR = 12

class CAPM:

    def __init__(self, stock, market_index, start_date, end_date, risk_free_rate):
        self.data = None
        self.stock = stock
        self.market_index = market_index
        self.start_date = start_date
        self.end_date = end_date
        self.risk_free_rate = risk_free_rate

    def download_data(self):
        data = {}
        # Add '.NS' suffix only for Indian stocks
        stock_ticker = self.stock if self.market_index not in ['^NSEI', '^BSESN'] else self.stock + '.NS'
        
        data['stock'] = yf.download(stock_ticker, self.start_date, self.end_date)['Adj Close']
        data['market'] = yf.download(self.market_index, self.start_date, self.end_date)['Adj Close']

        return pd.DataFrame(data)

    def initialize(self):
        stock_data = self.download_data()
        stock_data.index = pd.to_datetime(stock_data.index)  # Ensure index is datetime
        stock_data = stock_data.resample('M').last()  # Resample monthly

        self.data = pd.DataFrame({'s_adjclose': stock_data['stock'],
                                  'm_adjclose': stock_data['market']})

        # Logarithmic monthly returns
        self.data[['s_returns', 'm_returns']] = np.log(self.data[['s_adjclose', 'm_adjclose']] /
                                                       self.data[['s_adjclose', 'm_adjclose']].shift(1))

        # Remove the NaN values
        self.data = self.data.dropna()

    def calculate_beta(self):
        covariance_matrix = np.cov(self.data["s_returns"], self.data["m_returns"])
        beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]
        return beta

    def regression(self):
        beta, alpha = np.polyfit(self.data['m_returns'], self.data['s_returns'], deg=1)
        expected_return = self.risk_free_rate + beta * (self.data['m_returns'].mean() * MONTHS_IN_YEAR
                                                        - self.risk_free_rate)
        return beta, alpha, expected_return

    def get_regression_plot(self, alpha, beta):
        fig, axis = plt.subplots(figsize=(10, 5))  # Adjust size for better display
        axis.scatter(self.data["m_returns"], self.data['s_returns'], label="Data Points")
        axis.plot(self.data["m_returns"], beta * self.data["m_returns"] + alpha, color='red', label="CAPM Line")
        axis.set_title('Capital Asset Pricing Model, finding alpha and beta')
        axis.text(0.08, 0.05, r'$R_a = \beta * R_m + \alpha$', fontsize=18, transform=axis.transAxes)
        axis.set_xlabel('Market return $R_m$', fontsize=14)
        axis.set_ylabel('Stock return $R_a$', fontsize=14)
        axis.legend()
        axis.grid(True)
        return fig, axis
