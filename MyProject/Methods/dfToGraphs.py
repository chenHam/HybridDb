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
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../FilesAndInputs/mainCsv-smart.csv")
    dfS = pd.read_csv(path)
    column_values=exponential(df)
    print(column_values)
    column_valuesA=exponential(dfA)
    print(column_valuesA)
    column_valuesS=exponential(dfS)
    print(column_valuesS)
    df.insert(loc=0, column='new_column', value=column_values)
    dfA.insert(loc=0, column='new_column', value=column_valuesA)
    dfS.insert(loc=0, column='new_column', value=column_valuesS)
    data = df[['RunningTime','new_column']].plot('RunningTime','new_column',label="Fat",marker='',color='skyblue')
    dfA[['RunningTime','new_column']].plot('RunningTime','new_column',ax=data,label="Thin",marker='', color='olive')
    dfS[['RunningTime','new_column']].plot('RunningTime','new_column',ax=data,label="Smart",marker='', color='pink')
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
    return column_values

main()
