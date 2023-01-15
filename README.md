# Finance

# These codes are not investment tips. These are just starting points for further analysis.

yfinance_linear_regression.py  - plots the historical data and the predicted future price of a cryptocurrency using Linear Regression

random_forest.py - plots the historical data and the predicted future price of a cryptocurrency using Random Forest Regressor

trade_signal.py - Table citing the possibility of buying or selling an asset. The script then calculates and adds several technical indicators to the dataframe:

RSI (Relative Strength Indicator) which is a momentum indicator that compares the magnitude of recent gains to recent losses in an attempt to determine overbought and oversold conditions of an asset.<br>
MFI (Money Flow Index) which is a volume-weighted momentum indicator that uses both price and volume to measure buying and selling pressure.
EMA (Exponential Moving Average) which is a type of moving average that places a greater weight and significance on the most recent data points.
SMA (Simple Moving Average) which is a type of moving average that is calculated by summing up the closing prices for a certain number of time periods and then dividing the sum by the number of time periods.
The script then calculates the signal ('Buy', 'Sell' or 'Hold') for the current data point by comparing the closing price to the SMA_200 and the EMA_17 to the EMA_55, and the golden cross and death cross by comparing the SMA_200 and the EMA_17 to the EMA_55.

It also adds new columns to the dataframe with the calculated values for the indicators, signal, golden cross and death cross.
