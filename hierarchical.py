# Importing the libraries  
import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd  

# Importing the dataset  
dataset = pd.read_csv('Mall_Customers.csv')
x = dataset.iloc[:, [3, 4]].values  
#Finding the optimal number of clusters using the dendrogram  
import scipy.cluster.hierarchy as shc  
dendro = shc.dendrogram(shc.linkage(x, method="ward"))  
mtp.title("Dendrogrma Plot")  
mtp.ylabel("Euclidean Distances")  
mtp.xlabel("Customers")  
mtp.show()  

#training the hierarchical model on dataset  
from sklearn.cluster import AgglomerativeClustering  
hc= AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')  
y_pred= hc.fit_predict(x)  

#visulaizing the clusters  
mtp.scatter(x[y_pred == 0, 0], x[y_pred == 0, 1], s = 100, c = 'blue', label = 'Cluster 1')  
mtp.scatter(x[y_pred == 1, 0], x[y_pred == 1, 1], s = 100, c = 'green', label = 'Cluster 2')  
mtp.scatter(x[y_pred== 2, 0], x[y_pred == 2, 1], s = 100, c = 'red', label = 'Cluster 3')  
mtp.scatter(x[y_pred == 3, 0], x[y_pred == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')  
mtp.scatter(x[y_pred == 4, 0], x[y_pred == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')  
mtp.title('Clusters of customers')  
mtp.xlabel('Annual Income (k$)')  
mtp.ylabel('Spending Score (1-100)')  
mtp.legend()  
mtp.show()  



# Hierarchical clustering is another unsupervised machine learning algorithm, which is used to group the 
# unlabeled datasets into a cluster and also known as hierarchical cluster analysis or HCA.

# In this algorithm, we develop the hierarchy of clusters in the form of a tree,
# and this tree-shaped structure is known as the dendrogram.

# Agglomerative Hierarchical clustering
# The agglomerative hierarchical clustering algorithm is a popular example of HCA. To group the datasets into clusters, 
# it follows the bottom-up approach

# How the Agglomerative Hierarchical clustering Work?
# The working of the AHC algorithm can be explained using the below steps:

# Step-1: Create each data point as a single cluster.
# Step-2: Take two closest data points or clusters and merge them to form one cluster. 
# So, there will now be N-1 clusters.

# Step-3: Again, take the two closest clusters and merge them together to form one cluster. 
# There will be N-2 clusters.

# Repeat Step 3 until only one cluster left. So, we will get the following clusters. 
# Step-5: Once all the clusters are combined into one big cluster, develop the dendrogram 
# to divide the clusters as per the problem.


