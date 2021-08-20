#Import modules
import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from pandas_datareader import data

#Get any stock's data
def get_stock_data(ticker, start, end):
    stock_data = data.DataReader(ticker, start=start, end=end, data_source='yahoo')['Close']
    return stock_data



#Predict prices
def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))

    #3 different models to predict prices
    svr_lin = SVR(kernel = 'linear', C = 1e3)
    svr_poly = SVR(kernel = 'poly', C = 1e3, degree = 2)
    svr_rbf = SVR(kernel = 'rbf', C = 1e3, gamma = 0.1) #Radial Basis Function

    #Fit the data
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    #Plot the data using matplotlib
    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF Model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear Model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial Model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    #Return the predicted values
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

#Getting all data and extracting dates and values
dates_raw = get_stock_data('AAPL', '2021-08-01', '2021-08-18').index.tolist()
dates = []
for x in range(len(dates_raw)):
    dates.append(str(dates_raw[x].date()))
days = []
for x in dates:
    days.append(int(x.split('-')[2]))

prices = get_stock_data('AAPL', '2021-08-01', '2021-08-18').tolist()


#Predict price and print to console
predicted_price = predict_prices(days, prices, [[19]])
print(predicted_price)
