import pandas as pd
import os.path
import csv
import sys
def getPrediction(time):
    time = int(time)
    time=fixTimeNumber(time)
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../FilesAndInputs/runningTimeDistribution.csv")
    main_df = pd.read_csv(path)
    res = main_df.loc[main_df['RunningTime'] == time]
    if res is None:
        return "fat"
    else:
        return res['cluster_type'].values[0]

def fixTimeNumber(time):
    num=(int((time/10))*10)+10
    return num

