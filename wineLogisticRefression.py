from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the Wine dataset
wine = load_wine()
# Features
X = wine.data
# Target variable (wine quality)
y = wine.target
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize the Logistic Regression model
model = LogisticRegression()
# Train the model on the training data
model.fit(X_train, y_train)
# Make predictions on the test data
predictions = model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)



# Logistic regression is one of the most popular Machine Learning algorithms, 
# which comes under the Supervised Learning technique. 
# It is used for predicting the categorical dependent variable using a given set of independent variables.
# Logistic regression predicts the output of a categorical dependent variable. 
# Therefore the outcome must be a categorical or discrete value. 
# It can be either Yes or No, 0 or 1, true or False, etc. 
# but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lie between 0 and 1.

# Logistic Regression is much similar to the Linear Regression except that how they are used. 
# Linear Regression is used for solving Regression problems, 
# whereas Logistic regression is used for solving the classification problems.

# In Logistic regression, instead of fitting a regression line, we fit an "S" 
# shaped logistic function, which predicts two maximum values (0 or 1).


# # Logistic Function (Sigmoid Function):
# # The sigmoid function is a mathematical function used to map the predicted values to probabilities.
# # It maps any real value into another value within a range of 0 and 1.
# # The value of the logistic regression must be between 0 and 1, which cannot go beyond this limit, 
# so it forms a curve like the "S" form. 
# The S-form curve is called the Sigmoid function or the logistic function.
# # In logistic regression, we use the concept of the threshold value, which defines the probability of either 0 or 1. 
# Such as values above the threshold value tends to 1, and a value below the threshold values tends to 0.

# Assumptions for Logistic Regression:
# The dependent variable must be categorical in nature.
# The independent variable should not have multi-collinearity.