import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn import metrics  
import seaborn as sns  
from sklearn.datasets import load_iris  
from sklearn.model_selection import train_test_split  
from sklearn import tree  

# Loading the dataset  
iris = load_iris()  
#converting the data to a pandas dataframe  
data = pd.DataFrame(data = iris.data, columns = iris.feature_names)  
#creating a separate column for the target variable of iris dataset   
data['Species'] = iris.target  
#replacing the categories of target variable with the actual names of the species  
target = np.unique(iris.target)  
target_n = np.unique(iris.target_names)  
target_dict = dict(zip(target, target_n))  
data['Species'] = data['Species'].replace(target_dict)  
# Separating the independent dependent variables of the dataset  
x = data.drop(columns = "Species")  
y = data["Species"]  
names_features = x.columns  
target_labels = y.unique()  
# Splitting the dataset into training and testing datasets  
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 93)  
# Importing the Decision Tree classifier class from sklearn  
from sklearn.tree import DecisionTreeClassifier  
# Creating an instance of the classifier class  
dtc = DecisionTreeClassifier(max_depth = 3, random_state = 93)  
# Fitting the training dataset to the model  
dtc.fit(x_train, y_train)  
# Plotting the Decision Tree  
plt.figure(figsize = (30, 10), facecolor = 'b')  
Tree = tree.plot_tree(dtc, feature_names = names_features, class_names = target_labels, rounded = True, filled = True, fontsize = 14)  
plt.show()  
y_pred = dtc.predict(x_test)  
# Finding the confusion matrix  
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)  
matrix = pd.DataFrame(confusion_matrix)  
axis = plt.axes()  
sns.set(font_scale = 1.3)  
plt.figure(figsize = (10,7))  
# Plotting heatmap  
sns.heatmap(matrix, annot = True, fmt = "g", ax = axis, cmap = "magma")  
axis.set_title('Confusion Matrix')  
axis.set_xlabel("Predicted Values", fontsize = 10)  
axis.set_xticklabels([''] + target_labels)  
axis.set_ylabel( "True Labels", fontsize = 10)  
axis.set_yticklabels(list(target_labels), rotation = 0)  
plt.show()  






# Decision Tree is a Supervised learning technique that can be used for both classification and Regression problems, 
# but mostly it is preferred for solving Classification problems. 

# It is a tree-structured classifier, where internal nodes represent the features of a dataset, 
# branches represent the decision rules and each leaf node represents the outcome.

# In a Decision tree, there are two nodes, which are the Decision Node and Leaf Node. 
# Decision nodes are used to make any decision and have multiple branches, 
# whereas Leaf nodes are the output of those decisions and do not contain any further branches.

# The decisions or the test are performed on the basis of features of the given dataset.

# It is called a decision tree because, similar to a tree, it starts with the root node, 
# which expands on further branches and constructs a tree-like structure.
# In order to build a tree, we use the CART algorithm, which stands for 
# Classification and Regression Tree algorithm.

# How does the Decision Tree algorithm Work?
# In a decision tree, for predicting the class of the given dataset, the algorithm starts 
# from the root node of the tree. 
# This algorithm compares the values of root attribute with the record (real dataset) attribute and, 
# based on the comparison, follows the branch and jumps to the next node.

# For the next node, the algorithm again compares the attribute value with the other sub-nodes and move further. 
# It continues the process until it reaches the leaf node of the tree. 
# The complete process can be better understood using the below algorithm:
# Step-1: Begin the tree with the root node, says S, which contains the complete dataset.
# Step-2: Find the best attribute in the dataset using Attribute Selection Measure (ASM).
# Step-3: Divide the S into subsets that contains possible values for the best attributes.
# Step-4: Generate the decision tree node, which contains the best attribute.
# Step-5: Recursively make new decision trees using the subsets of the dataset created in step -3. 
# Continue this process until a stage is reached where you cannot further classify the nodes 
# and called the final node as a leaf node.