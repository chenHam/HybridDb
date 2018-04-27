import pandas as pd
import sys

input = '40'
def getPrediction(time):
    print("the value for chen: ", time)
    time = int(time)
    time=fixTimeNumber(time)
    main_df = pd.read_csv('Result.csv')
    res = main_df.loc[main_df['RunningTime'] == time]
    if res is None:
        return "fat"
    else:
        print(res['RunningTime'].values[0])
        return res['cluster_type'].values[0]

def fixTimeNumber(time):
    num = ((time/10)*10)+10
    return num

