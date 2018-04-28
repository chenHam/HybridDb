import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


all_df = pd.read_csv('mainCsv.csv')
all_df['RunningTime'] = pd.DatetimeIndex(all_df['RunningTime']).hour + (pd.DatetimeIndex(all_df['RunningTime']).minute)/100
# all_df['RunningTime'] = all_df['RunningTime'].day

all_df['Total'] = all_df['A'] + all_df['B'] + all_df['C']
all_df['AverageRunTime'] = (all_df['SumOfRunning'] / all_df['Total'])

# all_df.to_csv('main_formatted.csv', index=False)

df = all_df[['RunningTime', 'AverageRunTime']]

model = KMeans(n_clusters=3)
model.fit(df)
predict = model.predict(df)
x = model.fit_predict(df)
df["cluster"] = x
print(df)


fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(df['RunningTime'], df['AverageRunTime'],
                     c=pd.DataFrame(predict)[0], s=50)
ax.set_title('K-Means Clustering')
ax.set_xlabel('Timestamp')
ax.set_ylabel('AverageRunTime')
plt.colorbar(scatter)

print()
