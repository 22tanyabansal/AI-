# Basic packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Sklearn modules & classes
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn import metrics
bc = datasets.load_breast_cancer()
X = bc.data
y = bc.target
# Create training and test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
# Instantiate the Support Vector Classifier (SVC)
svc = SVC(C=1.0, random_state=1, kernel='linear')
# Fit the model
svc.fit(X_train, y_train)
# Make the predictions
y_predict = svc.predict(X_test)
# Measure the performance
print("Accuracy score %.3f" %metrics.accuracy_score(y_test, y_predict))


# Support Vector Machine
# Support Vector Machine (SVM) is a supervised machine learning algorithm used for both classification and regression. 
# Though we say regression problems as well it’s best suited for classification. 
# The main objective of the SVM algorithm is to find the optimal hyperplane in an N-dimensional space that can separate the data points in different classes in the feature space. 
# The hyperplane tries that the margin between the closest points of different classes should be as maximum as possible. 
# The dimension of the hyperplane depends upon the number of features. 
# If the number of input features is two, then the hyperplane is just a line. 
# If the number of input features is three, then the hyperplane becomes a 2-D plane. 
# It becomes difficult to imagine when the number of features exceeds three. 

# Types of Support Vector Machine
# Based on the nature of the decision boundary, Support Vector Machines (SVM) can be divided into 
# two main parts:

# Linear SVM: Linear SVMs use a linear decision boundary to separate the data points of different classes. 
# When the data can be precisely linearly separated, linear SVMs are very suitable. 
# This means that a single straight line (in 2D) or a hyperplane (in higher dimensions) can entirely divide the data points into their respective classes. 
# A hyperplane that maximizes the margin between the classes is the decision boundary.

# Non-Linear SVM: Non-Linear SVM can be used to classify data when it cannot be separated into two classes by a straight line (in the case of 2D). 
# By using kernel functions, nonlinear SVMs can handle nonlinearly separable data. 
# The original input data is transformed by these kernel functions into a higher-dimensional feature space, where the data points can be linearly separated. 
# A linear SVM is used to locate a nonlinear decision boundary in this modified space. 

# SVM implementation in Python
# Predict if cancer is Benign or malignant. 
# Using historical data about patients diagnosed with cancer enables doctors to 
# differentiate malignant cases and benign ones are given independent attributes.
# Steps
# Load the breast cancer dataset from sklearn.datasets
# Separate input features and target variables.
# Buil and train the SVM classifiers using RBF kernel.
# Plot the scatter plot of the input features.
# Plot the decision boundary.
# Plot the decision boundary