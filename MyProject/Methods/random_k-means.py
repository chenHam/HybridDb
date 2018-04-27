from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import pandas as pd


def Run():
    # experiment num 1
    file_name_fat = '/Users/barbrownshtein/PycharmProjects/FinalProject/HybridDb/MyProject/FilesAndInputs/Clustering_fat.csv'
    file_name_thin = '/Users/barbrownshtein/PycharmProjects/FinalProject/HybridDb/MyProject/FilesAndInputs/Clustering_thin.csv'
    #file_name_thin = 'mainCsv-thin-1.csv'

    df_fat = cluster_by_shows(file_name_fat)[['RunningTime', 'SumOfRunning']]
    df_fat['cluster_type'] = 'fat'
    df_thin = cluster_by_shows(file_name_thin)[['RunningTime', 'SumOfRunning']]
    df_thin['cluster_type'] = 'thin'

    final_df = pd.concat([df_fat, df_thin])
    print(final_df)

    df_result = final_df.groupby('RunningTime', as_index=False).apply(func).reset_index(drop=True)

    df_result.to_csv('runningTimeDistribution.csv', index=False)


def func(group):
    return group.loc[group['SumOfRunning'] == group['SumOfRunning'].min()]


def cluster_by_shows(file_name):
    main_df = pd.read_csv(file_name)
    # df = pd.read_csv('Clustering.csv')

    main_df['RunningTime'] = pd.DatetimeIndex(main_df['RunningTime']).hour + (pd.DatetimeIndex(main_df['RunningTime']).minute) / 100
    main_df['RunningTime'] = (main_df.index + 1) * 10
    print(main_df)
    df = main_df[['RunningTime', 'A', 'B']]
    # df['RunningTime'] = pd.DatetimeIndex(df['RunningTime']).hour + (pd.DatetimeIndex(df['RunningTime']).minute)/100

    range_n_clusters = [2, 3, 4, 5]
    # range_n_clusters = [2, 3, 4, 5, 6]

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
    df['cluster'] = x
    print(df)

    main_df['cluster'] = df['cluster']
    print(main_df)
    return main_df


Run()


