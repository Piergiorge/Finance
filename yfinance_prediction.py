import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Download historical data for Bitcoin
btc = yf.download("BTC-USD", start="2015-01-01", end="2023-01-13")

# Create a new DataFrame with only the 'Close' column
data = btc[['Close']]

# Create a variable to store the target column (future price)
# future_price = 7
future_price = 14

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

closing_prices = btc['Close'].values

# Plot the data
plt.plot(closing_prices, color='blue', label='Historical Data')
plt.plot(lr_prediction, color='red', label='Prediction')
plt.xlabel('Time')
plt.ylabel('Closing Price')
plt.title('Closing Prices of Cryptocurrency')
plt.show()
