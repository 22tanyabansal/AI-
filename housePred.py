
#https://studygyaan.com/data-science/linear-regression-machine-learning-project-for-house-price-prediction
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
df = pd.DataFrame(pd.read_csv("Housing.csv"))
# Preprocessing: Selecting features and target variable
X = df[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition']]
y = df['price']
# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Building the Linear Regression Model
model = LinearRegression()
# Fitting the model on the training data
model.fit(X_train, y_train)
# Model Evaluation
y_pred = model.predict(X_test)
# Mean Squared Error and R-squared for model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Linear Regression in Machine Learning
# Linear regression is one of the easiest and most popular Machine Learning algorithms. 
# It is a statistical method that is used for predictive analysis. Linear regression 
# makes predictions for continuous/real or numeric variables such as sales, salary, 
# age, product price, etc.

# Linear regression algorithm shows a linear relationship between a dependent (y) and one 
# or more independent (y) variables, hence called as linear regression. 
# Since linear regression shows the linear relationship, which means it finds how the value 
# of the dependent variable is changing according to the value of the independent variable.

# Mathematically, we can represent a linear regression as:
# y= a0+a1x+ ε
# Here,
# Y= Dependent Variable (Target Variable)
# X= Independent Variable (predictor Variable)
# a0= intercept of the line (Gives an additional degree of freedom)
# a1 = Linear regression coefficient (scale factor to each input value).
# ε = random error

# In the context of house price prediction, the dependent variable will be the house price, and the 
# independent variables can be factors like the size of the house, number of bedrooms, location, etc.

# House Price Prediction with Linear Regression Involves Following Steps:

# Dataset Collection: Gather historical house price data and corresponding features from platforms like Zillow or Kaggle.
# Data Preprocessing: Clean the data, handle missing values, and perform feature engineering, such as converting categorical variables to numerical representations.
# Splitting the Dataset: Divide the dataset into training and testing sets for model building and evaluation.
# Building the Model: Create a linear regression model to learn the relationships between features and house prices.
# Model Evaluation: Assess the model’s performance on the testing set using metrics like MSE or RMSE.
# Fine-tuning the Model: Adjust hyperparameters or try different algorithms to improve the model’s accuracy.
# Deployment and Prediction: Deploy the robust model into a real-world application for predicting house prices based on user inputs.