
# CAPM Analysis Tool

The CAPM (Capital Asset Pricing Model) Analysis Tool is a Streamlit-based web application that allows users to calculate the beta and expected return of a given stock based on the CAPM model. The tool is designed to be user-friendly and provides comprehensive insights into the stock's performance relative to the market index.

## Features

- **User Inputs**: Users can input the stock ticker, select the market index, specify the date range for the stock data, and enter the risk-free interest rate.
- **Market Indices**: Options include major indices like Nifty 50, Sensex, and S&P 500.
- **Indian Stocks**: For Indian stocks, users are advised to add `.NS` to the stock ticker.
- **Data Download**: Automatically downloads adjusted closing prices for the selected stock and market index.
- **Monthly Resampling**: Resamples the data to monthly frequency to calculate logarithmic returns.
- **Beta Calculation**: Calculates beta using both covariance and linear regression methods.
- **Expected Return**: Computes the expected annual return based on the CAPM formula.
- **Visualization**: Plots the CAPM regression line along with the data points.

## How to Use

1. **Enter Stock Ticker**: Input the stock ticker (e.g., HDFCBANK).
2. **Select Market Index**: Choose from the dropdown list of market indices (Nifty 50, Sensex, S&P 500).
3. **Set Date Range**: Select the start and end dates for the stock data to calculate returns.
4. **Risk-Free Rate**: Enter the risk-free interest rate (default is 0.05).
5. **Run Analysis**: Click the 'Run Analysis' button to perform the CAPM analysis and generate results.

## Example

Here is an example of how to use the tool:

- **Stock Ticker**: HDFCBANK
- **Market Index**: ^NSEI (Nifty 50)
- **Start Date**: 2020-01-01
- **End Date**: 2024-07-20
- **Risk-Free Rate**: 0.05

## Output

- **Calculated Beta**: Displays the beta calculated using the covariance matrix.
- **Beta from Regression**: Displays the beta obtained from linear regression.
- **Alpha from Regression**: Displays the alpha obtained from linear regression.
- **Expected Annual Return**: Shows the expected annual return calculated using the CAPM formula.
- **CAPM Regression Plot**: A scatter plot of the data points along with the CAPM regression line and the equation \( R_a = eta * R_m + lpha \).

## Deployment

The CAPM Analysis Tool can be accessed via the following Streamlit link: [CAPM Analysis Tool](https://capmodel.streamlit.app/)

## Installation

To run the application locally, follow these steps:

1. Clone the repository:
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Project Structure

- **app.py**: Main Streamlit application file.
- **capm.py**: Contains the CAPM class with methods for downloading data, calculating beta, performing regression, and plotting results.
- **requirements.txt**: List of required Python packages.
