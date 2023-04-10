# trade_R.R

This is a script written in R programming language to obtain the CCI (Commodity Channel Index) indicator for BTC-USD data obtained from Yahoo Finance, plot the candlestick chart along with the CCI indicator, and generate a buy/sell/hold signal based on the CCI value.

The script begins by loading the required libraries- `quantmod` and `lubridate`. It then specifies the start and end dates for which the data is to be fetched.
The `getSymbols()` function from `quantmod` package is then used to obtain the BTC-USD data from Yahoo Finance for the specified date range.
The `chartSeries()` function is used to plot the candlestick chart for the obtained data. The `addCCI()` function is used to calculate the CCI indicator and add it to the chart.

The CCI values are then extracted as a dataframe, and any missing values are replaced with 0. A signal is then generated based on the CCI value.
If the CCI is above 100, a sell signal is generated, if it is below -100, a buy signal is generated, and if it is between -100 and 100, a hold signal is generated.

The `'data'` and `'sinal'` columns are then extracted from the dataframe and converted into an xts object. The `chartSeries()` function is again used to plot the candlestick chart, and the `addTA()` function is used to plot the signal generated based on the CCI values.
The `addSMA()` function is used to add the Simple Moving Average lines for 9, 50, 100, and 200 periods.

Finally, the script saves the generated chart in the working directory.

# temporal.R

## Bitcoin Data Analysis
This script uses R and several packages to analyze and visualize Bitcoin data. The script performs the following tasks:

1 - Loads required packages
2 - Retrieves Bitcoin data from Yahoo Finance
3 - Creates a candlestick chart of Bitcoin price
4 - Decomposes Bitcoin price data into trend, seasonal, and random components using `decompose()` function
5 - Plots the decomposed components using `autoplot()` function
6 - Performs seasonal decomposition of time series data using `ggseasonplot()` function
7 - Plots candlestick chart of Bitcoin price for a specific time period using `chartSeries()` function

## Data source
Bitcoin price data is retrieved from Yahoo Finance using the `getSymbols()` function.

## Usage
To run this script, make sure all required packages are installed and loaded. Then, set the start and end dates for the Bitcoin price data using the start and end variables. Finally, run the script and observe the output.

## Output
The output of this script is a series of plots showing the decomposition of Bitcoin price data and the candlestick chart of Bitcoin price for a specific time period. The plots are saved in SVG format with the file names "`btcserie.svg`" and "`btcplot.svg`".
