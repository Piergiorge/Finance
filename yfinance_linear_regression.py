import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from datetime import date

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


# Create a new DataFrame with only the 'Close' and 'Volume' columns
data = crypt_data[['Close', 'Volume']]


# Create a new column that contains the target price
data['Prediction'] = data[['Close']].shift(-future_price)

# Create the feature and target arrays
X = np.array(data.drop(['Prediction'], 1))[:-future_price]
y = np.array(data['Prediction'])[:-future_price]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the linear regression model
lr = LinearRegression().fit(X_train, y_train)

# Test the model
lr_confidence = lr.score(X_test, y_test)
print("Linear Regression confidence: ", lr_confidence)

# Use the model to predict the future price
x_forecast = np.array(data.drop(['Prediction'], 1))[-future_price:]
lr_prediction = lr.predict(x_forecast)
print("Predicted Future Price: ", lr_prediction)

print(lr_prediction)

start= 1
end= future_price
plt.xlim(start, end)
short_hist = crypt_data['Close'].values

plt.plot(short_hist[-future_price:], color='blue', label='Historical Data')
plt.plot(lr_prediction, color='red', label='Prediction')
plt.xlabel('Time')
plt.ylabel('Closing Price')
plt.title(f'Closing Prices of {coin}')
plt.legend()
plt.show()
