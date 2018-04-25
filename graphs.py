import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('mainCsv-fat-1.csv')
dfA = pd.read_csv('mainCsv-thin-1.csv')
data = df[['RunningTime','SumOfRunning']].plot('RunningTime','SumOfRunning',label="Fat",marker='o',color='skyblue')
# dataA = dfA[['RunningTime','SumOfRunning']].plot('RunningTime','SumOfRunning',marker='o',color='olive')
dataA = dfA[['RunningTime','SumOfRunning']].plot('RunningTime','SumOfRunning',ax=data,label="Thin",marker='', color='olive')
plt.xlabel("Time from beginning")
plt.ylabel("Total time completed")
plt.show()

