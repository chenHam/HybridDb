import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


all_df = pd.read_csv('main.csv')

# all_df['A'] = all_df['A'].astype(np.float64)
# all_df['B'] = all_df['B'].astype(np.float64)
# all_df['C'] = all_df['C'].astype(np.float64)

all_df['Total'] = all_df['A'] + all_df['B'] + all_df['C']
all_df['AverageRunTime'] = (all_df['RunTime'] / all_df['Total'])

# all_df.to_csv('main_formatted.csv', index=False)

df = all_df[['Timestamp', 'AverageRunTime']]

model = KMeans(n_clusters=2)
model.fit(df)
predict = model.predict(df)
x = model.fit_predict(df)
df["cluster"] = x
print(df)



fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(df['Timestamp'], df['AverageRunTime'],
                     c=pd.DataFrame(predict)[0], s=50)
ax.set_title('K-Means Clustering')
ax.set_xlabel('Timestamp')
ax.set_ylabel('AverageRunTime')
plt.colorbar(scatter)

print()
