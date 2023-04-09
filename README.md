These codes are not investment tips. These are just starting points for further analysis.

# yfinance_linear_regression.py  - plots the historical data and the predicted future price of a cryptocurrency using Linear Regression

## Cryptocurrency Price Predictor - Linear Regression
This Python script uses linear regression to predict the future price of a given cryptocurrency.

To use the script, run it in a Python environment and enter the following information when prompted:

* Enter the cryptocurrency (Tick): The ticker symbol of the cryptocurrency you want to predict (e.g. BTC for Bitcoin).
* Enter the time (days): The number of days into the future you want to predict the price for.
* Is crypt? [Y]es or N[o]: Whether the cryptocurrency is listed in USD or another currency.

The script will then retrieve the historical price data, create a linear regression model, test the model, and make a prediction for the future price. Finally, it will plot the historical prices and the predicted price on a graph.

Note that this script makes several assumptions about the relationship between the features (closing price and volume) and the target variable (future closing price). In reality, the relationship may be much more complex and affected by other factors that are not included in the model. Therefore, the predictions should be taken with a grain of salt and used for informational purposes only.

# random_forest.py - plots the historical data and the predicted future price of a cryptocurrency using Random Forest Regressor

## Cryptocurrency Price Prediction - Random Forest
This script uses historical data of a cryptocurrency, obtained from Yahoo Finance, to predict its future price using a Random Forest Regression model. The script allows the user to input the cryptocurrency ticker symbol and the number of days into the future they want to predict the price for.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

```python
python random_forest.py
```
* Enter the cryptocurrency ticker symbol when prompted (e.g., BTC for Bitcoin).
* Enter the number of days into the future you want to predict the price for.
* If the cryptocurrency is not a USD-quoted coin, you will be asked to confirm.
* The script will download the historical data from Yahoo Finance and perform a Random Forest Regression on the data.
* The script will output the model's confidence score and the predicted future price.
* A chart of the historical and predicted prices will be displayed.


# trade_signal.py - Table citing the possibility of buying or selling an asset. The script then calculates and adds several technical indicators to the dataframe:

## Cryptocurrency Price Prediction - Trade Signal
This is a Python script that prompts the user to enter a cryptocurrency ticker, the number of days in the future to predict, and whether the cryptocurrency is a stock or a cryptocurrency. The start date is set to "`2015-01-01`" and the end date is set to the current date.

The script uses the Yahoo Finance API through the yfinance library to download historical price data for the specified cryptocurrency. It then calculates a number of technical indicators using the ta library, including:

* Relative Strength Index (RSI)
* Money Flow Index (MFI)
* Exponential Moving Averages (EMAs) with windows of 17, 55, and 200 days
* Simple Moving Average (SMA) with a window of 200 days
* The script also generates signals for buying, selling, or holding the cryptocurrency based on the EMA and SMA crossovers. A "Golden Cross" signal is generated when the 200-day SMA crosses above the 17-day EMA and the 55-day EMA. A "Death Cross" signal is generated when the 200-day SMA crosses below the 17-day EMA and the 55-day EMA.

* - Note that the signal generation needs to be fixed.
