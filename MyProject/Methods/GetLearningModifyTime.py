import pandas as pd
import sys
def getPrediction(time):
    time = int(time)
    time=fixTimeNumber(time)

    main_df = pd.read_csv("/Users/barbrownshtein/PycharmProjects/FinalProject/HybridDb/MyProject/FilesAndInputs/runningTimeDistribution.csv")
    res = main_df.loc[main_df['RunningTime'] == time]
    if res is None:
        return "fat"
    else:
        return res['cluster_type'].values[0]

def fixTimeNumber(time):
    num=((time/10)*10)+10
    return num

