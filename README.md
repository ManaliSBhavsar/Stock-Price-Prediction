# Stock-Price-Prediction

Predicting how the stock market will perform is one of the most difficult things to do. There are so many factors involved in the prediction – physical factors vs. psychological, rational and irrational behavior, etc. All these aspects combine to make share prices volatile and very difficult to predict with a high degree of accuracy.

The aim is to predict the future stock prices using the data from ‘N’ days. This dataset will be evaluated for better predictions using Natural Language Processing[NLP] and Machine Learning Techniques with Python to predict the future stock prices with high degree of accuracy.

# Approach used:
Using a Stock data set for a company which has date, opening rate, high rate, low rate, closing rate, total trade and total turnover.

# Implementation:
Collect the dataset (from Quandl), load the dataset and define the target variable for the problem.

Plotting the graph of the existing data using plotlib.

The profit or loss calculation is usually determined by the closing price of a stock for the day, hence considering the closing price as the target variable.

Using the moving average technique which uses the latest set of values for each prediction. For each subsequent step, the predicted values are taken into consideration while removing the oldest observed value from the set.

Create a data frame that contains only the Date and Close price columns, then split it into train and validation sets to verify our predictions.

Create predictions for the validation set and check the RMSE using the actual values.

Plot the predicted values along with the actual values.

# Result:
Prediction of stock market by using the TATA GLOBAL dataset of stock. Predicted the values for the dates that are present in the dataset by LSTM and then compare the predicted values with the actual values.
The Graph in orange is the predicted graph. The prediction is very close to the actual values(in green).
Achieved results with only 3.2% Error rate.
