import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_diabetes
# Load the diabetes dataset
diabetes = load_diabetes()
# Features (X) and target variable (y)
X = diabetes.data
y = diabetes.target
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize the RandomForestRegressor model
model = RandomForestRegressor(random_state=42)
# Train the model on the training data
model.fit(X_train, y_train)
# Make predictions on the test data
predictions = model.predict(X_test)
# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
# Calculate R-squared
r2 = r2_score(y_test, predictions)
print("R-squared:", r2)



# Random Forest is a popular machine learning algorithm that belongs to the supervised learning technique. 
# It can be used for both Classification and Regression problems in ML. 
# It is based on the concept of ensemble learning, which is a process of combining multiple 
# classifiers to solve a complex problem and to improve the performance of the model.

# The greater number of trees in the forest leads to higher accuracy and prevents the problem of overfitting.

# How does Random Forest algorithm work?
# Random Forest works in two-phase first is to create the random forest by combining N decision tree, and second is to make predictions for each tree created in the first phase.

# The Working process can be explained in the below steps and diagram:

# Step-1: Select random K data points from the training set.

# Step-2: Build the decision trees associated with the selected data points (Subsets).

# Step-3: Choose the number N for decision trees that you want to build.

# Step-4: Repeat Step 1 & 2.

# Step-5: For new data points, find the predictions of each decision tree, and assign the new data points to the category that wins the majority votes.


# Why use Random Forest?
# Below are some points that explain why we should use the Random Forest algorithm:

# It takes less training time as compared to other algorithms.
# It predicts output with high accuracy, even for the large dataset it runs efficiently.
# It can also maintain accuracy when a large proportion of data is missing.