import matplotlib.pyplot as plt
import pandas as pd
import os.path

def main():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../FilesAndInputs/mainCsv-fat.csv")
    df = pd.read_csv(path)
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../FilesAndInputs/mainCsv-thin.csv")
    dfA = pd.read_csv(path)
    column_values=exponential(df)
    print(column_values)
    column_valuesA=exponential(dfA)
    print(column_valuesA)
    df.insert(loc=0, column='new_column', value=column_values)
    dfA.insert(loc=0, column='new_column', value=column_valuesA)
    data = df[['RunningTime','new_column']].plot('RunningTime','new_column',label="Fat",marker='',color='skyblue')
    # dataA = dfA[['RunningTime','SumOfRunning']].plot('RunningTime','SumOfRunning',marker='o',color='olive')
    dataA = dfA[['RunningTime','new_column']].plot('RunningTime','new_column',ax=data,label="Thin",marker='', color='olive')
    plt.xlabel("Time from beginning")
    plt.ylabel("Total time completed")
    plt.show()


def exponential(df):
    list = df['SumOfRunning']
    column_values = []
    i = 0
    column_values.append(list[i])
    i += 1
    for l in list:
        if(i<len(list)):
            if (i != 0 ):
                sum = column_values[i - 1] + list[i]
                print(sum,column_values[i - 1],list[i])
                column_values.append(sum)
                i += 1
                # if(i==0):
                #     column_values.append(list[i])
                #     i+=1
    return column_values
# date=df['RunningTime']
    # datelist=[]
    # for d in date:
    #     datelist.append(d)
    # d = datelist[0].split(' ')
    # d[1].split('-')
