from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

iris_data = load_iris()  # Loading iris dataset from sklearn.datasets
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)  # Creating DataFrame

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=100, n_init=10, random_state=0)  # Applying KMeans classifier
y_kmeans = kmeans.fit_predict(iris_df)

print(kmeans.cluster_centers_)  # Display cluster centers

plt.scatter(iris_df.iloc[y_kmeans == 0, 0], iris_df.iloc[y_kmeans == 0, 1], s=100, c='red', label='Iris-setosa')
plt.scatter(iris_df.iloc[y_kmeans == 1, 0], iris_df.iloc[y_kmeans == 1, 1], s=100, c='blue', label='Iris-versicolour')
plt.scatter(iris_df.iloc[y_kmeans == 2, 0], iris_df.iloc[y_kmeans == 2, 1], s=100, c='green', label='Iris-virginica')  # Visualizing the clusters - On the first two columns
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='black', label='Centroids')  # Plotting the centroids of the clusters
plt.legend()
plt.show()





# K-Means Clustering is an Unsupervised Learning algorithm, which groups the unlabeled dataset into different clusters. 
# Here K defines the number of pre-defined clusters that need to be created in the process, as if K=2, there will be two clusters, 
# and for K=3, there will be three clusters, and so on.

# It is an iterative algorithm that divides the unlabeled dataset into k different clusters in such a way 
# that each dataset belongs only one group that has similar properties.

# How does the K-Means Algorithm Work?
# The working of the K-Means algorithm is explained in the below steps:

# Step-1: Select the number K to decide the number of clusters.

# Step-2: Select random K points or centroids. (It can be other from the input dataset).

# Step-3: Assign each data point to their closest centroid, which will form the predefined K clusters.

# Step-4: Calculate the variance and place a new centroid of each cluster.

# Step-5: Repeat the third steps, which means reassign each datapoint to the new closest centroid of each cluster.

# Step-6: If any reassignment occurs, then go to step-4 else go to FINISH.
# KMeans Clustering with Iris Dataset
#  K-means clustering is an Unsupervised machine learning algorithm. 

# First, choose the clusters K
# Randomly select k centroids from the whole dataset
# Assign all points to the closest cluster centroid
# Recompute centroids again for new clusters
# now repeat steps 3 and 4 until centroids converge