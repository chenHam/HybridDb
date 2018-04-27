import pandas as pd
import sys

input = '40'
time = int(input)
#time = sys.argv[1]

main_df = pd.read_csv('Result.csv')

res = main_df.loc[main_df['RunningTime'] == time]

print(res['cluster_type'].values[0])


