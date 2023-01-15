library(quantmod)
library(ggplot2)
library(forecast)
library(seasonal)
library(seasonalview)
library(tsbox)
library(zoo)

start <- as.Date("2020-11-1")
x <- as.character(Sys.time())
y <- (scan(text = x, what = ""))
y[[1]]
end <- as.Date(y[[1]])

#DATA
btcData <- getSymbols("BTC-USD", src = "yahoo", auto.assign = FALSE)
chartSeries(btcData, type = 'candlesticks', theme = 'white')

btcserie <- Cl(btcData)
class(btcserie)
btcserie <- ts_ts(btcserie)
btcserie <- na.fill(btcserie, 'extend')

x <- decompose(btcserie)
svg(filename = "btcserie.svg")
  autoplot(x)
dev.off()

# another tec
msap <- mstl(btcserie)
autoplot(msap)

ggseasonplot(btcserie)
ggseasonplot(btcserie, polar = T)

start <- as.Date("2020-11-1")
x <- as.character(Sys.time())
y <- (scan(text = x, what = ""))
y[[1]]
end <- as.Date(y[[1]])

#DATA
btcData <- getSymbols("BTC-USD", src = "yahoo", from = start, to = end, auto.assign = FALSE)
svg(filename = "btcplot.svg")
  chartSeries(btcData, type = 'candlesticks', theme = 'white')
dev.off()
  
