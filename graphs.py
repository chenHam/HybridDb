import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('mainCsv.csv')
dfA = pd.read_csv('mainCsvA.csv')
data = df[['RunningTime','SumOfRunning']].plot('RunningTime','SumOfRunning',marker='o',color='skyblue')
dataA = dfA[['RunningTime','SumOfRunning']].plot('RunningTime','SumOfRunning',marker='o',color='olive')
# dataA = dfA[['RunningTime','SumOfRunning']].plot('RunningTime','SumOfRunning',ax=data,marker='', color='olive')
plt.xlabel("Time from beginning")
plt.ylabel("Total time completed")
plt.show()

