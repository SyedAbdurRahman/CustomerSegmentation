import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# loading the data from csv file to a Pandas DataFrame
customer_data = pd.read_csv('Mall_Customers.csv')

# first 5 rows in the dataframe
customer_data.head()

# finding the number of rows and columns
customer_data.shape

# gettin some info about the dataset
customer_data.info()

# checking for missing values
customer_data.isnull().sum()

X = customer_data.iloc[:, [3, 4]].values
print(X)

# finding wcss val for diff no of clusters
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init ='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# plot an elbow graph

sns.set()
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++',random_state=0)

# return a label for each datapoint based on their cluster
Y = kmeans.fit_predict(X)
print(Y)

# plotting all the clusters and their centroids

plt.figure(figsize=(8, 8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=50, c='green', label='Cluster 1')
plt.scatter(X[Y==1,0], X[Y==1,1], s=50, c='red', label='Cluster 2')
plt.scatter(X[Y==2,0], X[Y==2,1], s=50, c='yellow', label='Cluster 3')
plt.scatter(X[Y==3,0], X[Y==3,1], s=50, c='violet', label='Cluster 4')
plt.scatter(X[Y==4,0], X[Y==4,1], s=50, c='blue', label='Cluster 5')

# plot the centroids

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='black', label='Centroids')

plt.title('Customer Clusters')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()