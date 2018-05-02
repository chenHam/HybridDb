from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import pandas as pd
import os.path


class X:
    def __init__(self):
        self.df, self.n_clusters_max = self.get_n_max_cluster('../FilesAndInputs/mainCsv-fat.csv')
        self.model = KMeans(n_clusters=self.n_clusters_max)
        self.model.fit(self.df)

    def predict(self, a_shows, b_shows):
        df = '[' + str(a_shows) + ',' + str(b_shows) + ']'
        predict = self.model.predict(df)
        return predict

    def Run(self):
        # experiment num 1
        file_name_fat = '../FilesAndInputs/mainCsv-fat.csv'
        file_name_thin = '../FilesAndInputs/mainCsv-thin.csv'
        # file_name_thin = 'mainCsv-thin-1.csv'

        df_fat = self.cluster_by_shows(file_name_fat)[['RunningTime', 'SumOfRunning', 'behaviourDistribution']]
        df_fat['technologyRecomendation'] = 'T1'
        # df_fat['D'] = 'D'
        # df_fat['behaviourDistribution'] = df_fat[['D','behaviourDistribution']]
        df_thin = self.cluster_by_shows(file_name_thin)[['RunningTime', 'SumOfRunning', 'behaviourDistribution']]
        df_thin['technologyRecomendation'] = 'T2'

        final_df = pd.concat([df_fat, df_thin])
        print(final_df)

        df_result = final_df.groupby('RunningTime', as_index=False).apply(self.func).reset_index(drop=True)

        df_result.to_csv('runningTimeDistribution.csv', index=False)

    def func(self, group):
        return group.loc[group['SumOfRunning'] == group['SumOfRunning'].min()]

    def run(self):
        predict = self.model.predict(self.df)
        x = self.model.fit_predict(self.df)
        self.df['behaviourDistribution'] = x
        print(self.df)
        self.df['D'] = 'D'

        self.main_df['behaviourDistribution'] = self.df[['D', 'behaviourDistribution']].astype(str).sum(axis=1)
        # main_df['behaviourDistribution'] = df['behaviourDistribution']
        print(self.main_df)
        # return self.main_df

        # experiment num 1
        file_name_fat = '../FilesAndInputs/Clustering_fat.csv'
        file_name_thin = '../FilesAndInputs/Clustering_thin.csv'
        # file_name_thin = 'mainCsv-thin-1.csv'

        df_fat = self.cluster_by_shows(file_name_fat)[['RunningTime', 'SumOfRunning', 'behaviourDistribution']]
        df_fat['technologyRecomendation'] = 'T1'

        df_thin = self.cluster_by_shows(file_name_thin)[['RunningTime', 'SumOfRunning', 'behaviourDistribution']]
        df_thin['technologyRecomendation'] = 'T2'

        final_df = pd.concat([df_fat, df_thin])
        print(final_df)

        df_result = final_df.groupby('RunningTime', as_index=False).apply(self.func).reset_index(drop=True)

        df_result.to_csv('runningTimeDistribution.csv', index=False)

    def func(self, group):
        return group.loc[group['SumOfRunning'] == group['SumOfRunning'].min()]

    def get_n_max_cluster(self, file_name):
        self.main_df = pd.read_csv(file_name)
        # df = pd.read_csv('Clustering.csv')

        self.main_df['RunningTime'] = pd.DatetimeIndex(self.main_df['RunningTime']).hour + (pd.DatetimeIndex(
            self.main_df['RunningTime']).minute) / 100
        self.main_df['RunningTime'] = (self.main_df.index + 1) * 10
        print(self.main_df)
        # df = main_df[['RunningTime', 'A', 'B']]
        df = self.main_df[['A', 'B']]

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
        return (df,n_clusters_max)

    def cluster_by_shows(self,file_name):
        main_df = pd.read_csv(file_name)

        main_df['RunningTime'] = (main_df.index + 1)
        print(main_df)
        df = main_df[['A', 'B']]

        range_n_clusters = [2, 3, 4, 5]
        # range_n_clusters = [2, 3, 4, 5, 6]

        model = KMeans(n_clusters=self.n_clusters_max)
        model.fit(df)
        predict = model.predict(df)
        x = model.fit_predict(df)
        df['behaviourDistribution'] = x
        print(df)
        df['D'] = 'D'

        main_df['behaviourDistribution'] = df[['D', 'behaviourDistribution']].astype(str).sum(axis=1)
        # main_df['behaviourDistribution'] = df['behaviourDistribution']
        print(main_df)
        return main_df

    # def bla(self):
    # #
    # # df_fat['A'] = pd.read_csv(file_name_fat)['A']
    # # df_fat['B'] = pd.read_csv(file_name_fat)['B']
    # #
    # # df_thin['A'] = pd.read_csv(file_name_thin)['A']
    # # df_thin['B'] = pd.read_csv(file_name_thin)['B']
    #
    # df_result = pd.read_csv('runningTimeDistribution.csv')
    # # df_result['distribution'] = 'none'
    # # df_result.to_csv('runningTimeDistribution.csv', index=True)
    #
    #
    # for i in range(0, 15):
    #     # a_shows = '2'
    #     # b_shows = '4'
    #     D = df_result.iloc[i]['behaviourDistribution']
    #     if (D == 'D1'):
    #         a_shows = df_fat.iloc[i]['A']
    #         b_shows = df_fat.iloc[i]['B']
    #     if (cluster_type == 'thin'):
    #         a_shows = df_thin.iloc[i]['A']
    #         b_shows = df_thin.iloc[i]['B']
    #     val = str(a_shows) + ',' + str(b_shows)
    #     df_result = df_result.set_value(i, 'distribution', value=val)

    def getPrediction(self,time):
        time = int(time)
        print('get prediction time: ', time)
        time = self.fixTimeNumber(time)
        print('fixed time: ', time)
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../FilesAndInputs/runningTimeDistribution.csv")
        main_df = pd.read_csv(path)
        res = main_df.loc[main_df['RunningTime'] == time]
        print('res: ', res)
        if res is None:
            return "fat"
        else:
            return res['cluster_type'].values[0]

    def fixTimeNumber(time):
        num = (int((time / 10)) * 10) + 10
        return num

kmeans = X()
kmeans.Run()


