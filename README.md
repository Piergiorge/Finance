These codes are not investment tips. These are just starting points for further analysis.

## yfinance_linear_regression.py  - plots the historical data and the predicted future price of a cryptocurrency using Linear Regression

# random_forest.py - plots the historical data and the predicted future price of a cryptocurrency using Random Forest Regressor

## Cryptocurrency Price Prediction
This script uses historical data of a cryptocurrency, obtained from Yahoo Finance, to predict its future price using a Random Forest Regression model. The script allows the user to input the cryptocurrency ticker symbol and the number of days into the future they want to predict the price for.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

```python
python predict_crypto_price.py
```
* Enter the cryptocurrency ticker symbol when prompted (e.g., BTC for Bitcoin).
* Enter the number of days into the future you want to predict the price for.
* If the cryptocurrency is not a USD-quoted coin, you will be asked to confirm.
* The script will download the historical data from Yahoo Finance and perform a Random Forest Regression on the data.
* The script will output the model's confidence score and the predicted future price.
* A chart of the historical and predicted prices will be displayed.


# trade_signal.py - Table citing the possibility of buying or selling an asset. The script then calculates and adds several technical indicators to the dataframe:

* RSI (Relative Strength Indicator) which is a momentum indicator that compares the magnitude of recent gains to recent losses in an attempt to determine overbought and oversold conditions of an asset.<br>
* MFI (Money Flow Index) which is a volume-weighted momentum indicator that uses both price and volume to measure buying and selling pressure.<br>
* EMA (Exponential Moving Average) which is a type of moving average that places a greater weight and significance on the most recent data points.<br>
* SMA (Simple Moving Average) which is a type of moving average that is calculated by summing up the closing prices for a certain number of time periods and then dividing the sum by the number of time periods.<br>
The script then calculates the signal (`'Buy'`, `'Sell'` or `'Hold'`) for the current data point by comparing the closing price to the `SMA_200` and the `EMA_17` to the `EMA_55`, and the `golden cross` and `death cross` by comparing the `SMA_200` and the `EMA_17` to `the EMA_55`.

It also adds new columns to the dataframe with the calculated values for the indicators, signal, golden cross and death cross.
