import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv("customer_data.csv")
features = data[['Age', 'Income']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
optimal_clusters = 3
# Perform K-Means clustering
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(scaled_features)
# Add cluster labels to the original data
data['Cluster'] = cluster_labels
# Print and analyze the clusters
for cluster in range(optimal_clusters):
    print(f"Cluster {cluster}:")
    print(data[data['Cluster'] == cluster][['Age', 'Income']])
    print("--------------------------")

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

# Step-7: The model is ready.

# The steps to be followed for the implementation are given below:
# Data Pre-processing
# Finding the optimal number of clusters using the elbow method
# Training the K-means algorithm on the training dataset
# Visualizing the clusters