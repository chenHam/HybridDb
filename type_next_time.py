import pandas as pd


def get_prediction(time_str):
    # input = '40'
    # time = sys.argv[1]
    time = int(time_str)

    main_df = pd.read_csv('Result.csv')

    res = main_df.loc[main_df['RunningTime'] == time]
    if res is None:
        return "error"

    print(res['cluster_type'].values[0])
    return res['cluster_type'].values[0]

