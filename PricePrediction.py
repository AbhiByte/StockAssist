"""
SVM Regression for stock data.
"""

#Import modules
import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from pandas_datareader import data

#Get any stock's data
def get_stock_data(ticker, start, end):
    """
    :param ticker:
        Ticker symbol, ex. AAPL.
    :param start:
        Start date.
    :param end:
        End date.
    """
    stock_data = data.DataReader(ticker, start=start, end=end, data_source='yahoo')['Close']
    return stock_data

#Predict prices
def predict_prices(dates, prices, x):
    """
    :param dates:
        List of dates.
    :param prices:
        List of prices.
    """
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



if __name__ == "__main__":
    #Getting all data and extracting dates and values
    symbol = str(input('Enter the ticker symbol: '))
    start = str(input('Enter the starting date (YYYY-MM-DD): '))
    end = str(input('Enter the ending date (YYYY-MM-DD): '))
    dates_raw = get_stock_data(symbol, start, end).index.tolist()
    dates = []
    for x in range(len(dates_raw)):
        dates.append(str(dates_raw[x].date()))
    days = []
    for x in dates:
        days.append(int(x.split('-')[2]))
    
    prices = get_stock_data(symbol, start, end).tolist()
    
    
    #Predict price and print to console
    next_day = int(end.split('-')[2]) + 1
    predicted_price = predict_prices(days, prices, [[next_day]])
    print(predicted_price)
