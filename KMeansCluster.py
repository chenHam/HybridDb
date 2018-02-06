import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


df = pd.read_csv('kmeansQueries.csv', header=None)
model = KMeans(n_clusters=4)
model.fit(df)
x=model.fit_predict(df)
df["cluster"]=x
print(df)
