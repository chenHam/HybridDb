from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import pandas as pd

df = pd.read_csv('Clustering1.csv')
df['RunningTime'] = pd.DatetimeIndex(df['RunningTime']).hour + (pd.DatetimeIndex(df['RunningTime']).minute)/100
df = df[['RunningTime', 'A', 'B', 'C']].values
# df['RunningTime'] = pd.DatetimeIndex(df['RunningTime']).hour + (pd.DatetimeIndex(df['RunningTime']).minute)/100

range_n_clusters = [2, 3, 4, 5]
#range_n_clusters = [2, 3, 4, 5, 6]

silhouette_avg_max = 0
n_clusters_max = 0

for n_clusters in range_n_clusters:
    # Initialize the clusterer with n_clusters value and a random generator
    # seed of 10 for reproducibility.
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(df)

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = silhouette_score(df, cluster_labels)

    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)

    if silhouette_avg_max < silhouette_avg:
        silhouette_avg_max = silhouette_avg
        n_clusters_max = n_clusters

    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(df, cluster_labels)


print("n_cluster_max = ", n_clusters_max)

model = KMeans(n_clusters=n_clusters_max)
model.fit(df)
predict = model.predict(df)
x = model.fit_predict(df)
df["cluster"] = x
print(df)


