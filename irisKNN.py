#https://github.com/kshitizrohilla/iris-flower-classification-using-k-nearest-neighbor-algorithm/blob/main/notebook.ipynb

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris

# Load the Iris dataset from scikit-learn
iris = load_iris()
# Extract features (X) and target variable (y)
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(y_pred)
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)



# K-Nearest Neighbour is one of the simplest Machine Learning algorithms based on Supervised Learning technique.
# K-NN algorithm assumes the similarity between the new case/data and 
# available cases and put the new case into the category that is most similar 
# to the available categories.
# K-NN is a non-parametric algorithm, which means it does not make any assumption on underlying data.
# It is also called a lazy learner algorithm because it does not learn from the training set immediately 
# instead it stores the dataset and at the time of classification, it performs an action 
# on the dataset.

# How does K-NN work?
# The K-NN working can be explained on the basis of the below algorithm:

# Step-1: Select the number K of the neighbors
# Step-2: Calculate the Euclidean distance of K number of neighbors
# Step-3: Take the K nearest neighbors as per the calculated Euclidean distance.
# Step-4: Among these k neighbors, count the number of the data points in each category.
# Step-5: Assign the new data points to that category for which the number of the neighbor is maximum.
# Step-6: Our model is ready.


# How to select the value of K in the K-NN Algorithm?
# Below are some points to remember while selecting the value of K in the K-NN algorithm:

# There is no particular way to determine the best value for "K", so we need to try some values to find the best out of them. The most preferred value for K is 5.
# A very low value for K such as K=1 or K=2, can be noisy and lead to the effects of outliers in the model.
# Large values for K are good, but it may find some difficulties.