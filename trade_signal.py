import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import ta

while True:
    coin = input('Enter the cryptocurrency (Tick): ') # ex : BTC for Bitcoin
    future_price = input('Enter the time (days): ') # ex : 5
    current_date = date.today().strftime("%Y-%m-%d")
    choice = input("Is crypt? [Y]es or N[o]")
    if coin and coin.isalpha() and future_price.isdigit() and choice:
        coin = coin.upper()
        coin_search = coin
        future_price = int(future_price)
        if choice.upper() == 'Y':
            coin_search = f'{coin}-USD'
        try:
            crypt_data = yf.download(coin_search, start="2015-01-01", end=current_date)
            print(f'Historical data for {coin} from {crypt_data.index[0]} to {crypt_data.index[-1]}')
            break
        except ValueError:
            print(f'{coin} not found or no data available')
    else:
        print("Invalid input")
        
rsi = ta.momentum.RSIIndicator(crypt_data['Close'], window=14)
mfi = ta.volume.MFIIndicator(crypt_data['High'], crypt_data['Low'], crypt_data['Close'], crypt_data['Volume'], window=14)
ema_17 = ta.trend.EMAIndicator(crypt_data['Close'], window= 17)
ema_55 = ta.trend.EMAIndicator(crypt_data['Close'], window= 55)
ema_200 = ta.trend.EMAIndicator(crypt_data['Close'], window= 200)
sma_200 = ta.trend.SMAIndicator(crypt_data['Close'], window= 200)

crypt_data['ema_17'] = ema_17.ema_indicator()
crypt_data['ema_55'] = ema_55.ema_indicator()
crypt_data['ema_200'] = ema_200.ema_indicator()
crypt_data['sma_200'] = sma_200.sma_indicator()
crypt_data['mfi'] = mfi.money_flow_index()
crypt_data['rsi'] = rsi.rsi()

# need to fix
crypt_data['Signal'] = np.where((crypt_data['Close'] > crypt_data['sma_200']) & (crypt_data['ema_17'] > crypt_data['ema_55']), 'Buy',
                                np.where((crypt_data['Close'] < crypt_data['sma_200']) & (crypt_data['ema_17'] < crypt_data['ema_55']), 'Sell', 'Hold'))


# gold and death
crypt_data['Golden Cross'] = np.where((crypt_data['sma_200'] > crypt_data['Close']) & (crypt_data['ema_17'] > crypt_data['ema_55']), True, False)
crypt_data['Death Cross'] = np.where((crypt_data['sma_200'] < crypt_data['Close']) & (crypt_data['ema_17'] < crypt_data['ema_55']), True, False)
