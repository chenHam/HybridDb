import pandas as pd
import os.path
import csv
import sys
def getPrediction(time):
    time = int(time)
    print('get prediction time: ', time)
    time=fixTimeNumber(time)
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
    num=(int((time/10))*10)+10
    return num

