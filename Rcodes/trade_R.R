library(quantmod)
library(lubridate)

start <- as.Date("2021-1-1")

#DATA
x <- as.character(Sys.time())
y <- (scan(text = x, what = ""))
y[[1]]
end <- as.Date(y[[1]])

btcData <- getSymbols("BTC-USD", src = "yahoo", from = start, to = end, auto.assign = FALSE)

chartSeries(btcData, type = 'candlesticks', theme = 'white', TA=NULL) # sem volume
addCCI(n=20, maType = 'SMA', c=0.015) # muito bom

indicador = CCI(HLC(btcData), n=20, maType = 'SMA',c = 0.015)

indicador = as.data.frame(indicador)
indicador[is.na(indicador)] = 0

# +100 imply an overbought condition, while readings below ???100 imply an oversold condition
# 1 buy
# -1 sell
# 0 hold

indicador['sinal'] = ifelse( indicador['cci'] > 100, -1,   #### vender 
                             ifelse(indicador['cci']< -100, 1,0  ) )

indicador['data'] = as_date(row.names(indicador))

indicador = indicador[, 2:3]
rownames(indicador) <- NULL

sinal = as.xts(indicador[,1], order.by = indicador[,2])
class(sinal)
#plot (sinal)
#chartSeries(btcData, type = 'candlesticks', theme = 'white', TA=NULL) # sem volume
chartSeries(btcData, type = 'candlesticks', theme = 'white') # sem volume
addTA(sinal, type = "S", col = 'red', lwd = 2, legend = "Sinal de compra??? ou venda???")
addSMA(n=9, with.col = Cl, overlay = T, col = 'green') # muito bom
addSMA(n=50, with.col = Cl, overlay = T, col = 'cyan') # muito bom
addSMA(n=100, with.col = Cl, overlay = T, col = 'red') # muito bom
addSMA(n=200, with.col = Cl, overlay = T, col = 'black') # muito bom
