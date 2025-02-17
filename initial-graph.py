#import packages
import pandas as pd
import numpy as np
#from pyramid.arima import auto_arima
#to plot within notebook
import matplotlib.pyplot as plt
#%matplotlib inline
#from pyramid.arima import auto_arima
#importing required libraries
from sklearn.preprocessing import MinMaxScaler
#import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, LSTM
#setting figure size
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10
#for normalizing data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
#read the file
df = pd.read_csv('NSE-TATAGLOBAL1.csv')
#print the head
df.head()
#setting index as date
df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index = df['Date']
#plot
plt.figure(figsize=(16,8))
plt.plot(df['Close'], label='Close Price history')
data = df.sort_index(ascending=True, axis=0)
train = data[:987]
valid = data[987:]
training = train['Close']
validation = valid['Close']
model = auto_arima(training, start_p=1, start_q=1,max_p=3, max_q=3, m=12,start_P=0, seasonal=True,d=1, D=1, trace=True,error_action='ignore',suppress_warnings=True)
model.fit(training)
forecast = model.predict(n_periods=248)
forecast = pd.DataFrame(forecast,index = valid.index,columns=['Prediction'])
#plot
plt.plot(train['Close'])
plt.plot(valid['Close'])
plt.plot(forecast['Prediction'])
