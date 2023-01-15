import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
import matplotlib.pyplot as plt
from datetime import date

while True:
    coin = input('Enter the cryptocurrency (Tick): ') # ex : BTC for Bitcoin
    future_price = input('Enter the time (days): ') # ex : 5
    current_date = date.today().strftime("%Y-%m-%d")
    if coin and coin.isalpha() and future_price.isdigit(): 
        coin = coin.upper()
        future_price = int(future_price)
        coin_search = f'{coin}-USD'
        try:
            crypt_data = yf.download(coin_search, start="2015-01-01", end=current_date)
            print(f'Historical data for {coin} from {crypt_data.index[0]} to {crypt_data.index[-1]}')
            break
        except ValueError:
            print(f'{coin} not found or no data available')
    else:
        print("Invalid input")
        
data = crypt_data[['Close', 'Volume', 'High', 'Low']]

# Create a new column that contains the target price
data['Prediction'] = data[['Close']].shift(-future_price)

# Create the feature and target arrays
X = np.array(data.drop(['Prediction'], 1))[:-future_price]
y = np.array(data['Prediction'])[:-future_price]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the model and the parameter grid
rfr = RandomForestRegressor(random_state=0)
param_grid = {'n_estimators': [50, 100, 200],
              'max_depth': [5, 10, 15],
              'min_samples_split': [2, 4, 8],
              'min_samples_leaf': [1, 2, 4]}

# Perform randomized search for hyperparameter tuning
rfr_random = RandomizedSearchCV(estimator=rfr, param_distributions=param_grid, n_iter=100, cv=5, verbose=2, random_state=0)
rfr_random.fit(X_train, y_train)

# Test the model
rfr_confidence = rfr_random.score(X_test, y_test)
print("Random Forest Regression confidence: ", rfr_confidence)

# Use the model to predict the future price
x_forecast = np.array(data.drop(['Prediction'], 1))[-future_price:]
rfr_prediction = rfr_random.predict(x_forecast)
print("Predicted Future Price: ", rfr_prediction)

start= 1
end= future_price
plt.xlim(start, end)
short_hist = crypt_data['Close'].values
plt.plot(short_hist[-future_price:], color='blue', label='Historical Data')
plt.plot(rfr_prediction, color='red', label='Prediction')
plt.xlabel('Time')
plt.ylabel('Closing Price')
plt.title('Closing Prices of Cryptocurrency')
plt.legend()
plt.show()
