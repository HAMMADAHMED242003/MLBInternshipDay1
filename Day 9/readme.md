## What is Clustering?

Clustering is an unsupervised machine learning technique that groups similar data into different clusters. In this project, I used K-Means clustering to group the Iris flowers based on their features.

## What is PCA?

PCA (Principal Component Analysis) is a technique used to reduce the number of features in a dataset while keeping most of the important information. In this project, I reduced the 4 original features to 2 principal components (PC1 and PC2) so the data could be visualized easily.

## How did you determine the best value of K?

I used the Elbow Method to find the best value of K. I plotted the WCSS values for K from 1 to 10 and observed that the graph had an elbow at K = 3, so I selected 3 clusters.

## What insights did you gain from the visualizations?
1. The Elbow Method showed that 3 is the best number of clusters.
2. K-Means grouped the Iris flowers into three clusters.
3. PCA made it easier to visualize the data by reducing it from 4 features to 2 principal components.
4. The PCA graph showed the clusters more clearly than the original data.