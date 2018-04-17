import powerSetFinder as psf;
import csv;
import pandas as pd;
import datetime;

def ortal_main(mainCsv,hour,df):

    startTime = hour
    total = df['RunTime'].sum()
    queries_type = df['QueryType']

    counterS = 0
    counterU = 0
    counterI = 0

    for type in queries_type:
        if type == 0:
            counterS+=1
        if type == 1:
            counterU+=1
        if type == 2:
            counterI+=1

    mainCsv = mainCsv.append(pd.Series([startTime, counterS, counterU, counterI, total], index=['RunningTime','A','B','C','SumOfRunning']),ignore_index=True)
    return mainCsv

def test():
    for t in total:
        listsum.append(t)
    listsum.remove('RunTime')

    query = df[3]
    listquery = []
    for q in query:
        listquery.append(q)
    listquery.remove("Query")

    counterS=0
    counterU=0
    counterI=0
    for l in listquery:
        cluster = l.split(" ")
        if(str(cluster[0]).lower() == 'select'):
            counterS+=1
        if(str(cluster[0]).lower() == 'update'):
            counterU+=1
        if (str(cluster[0]).lower() == 'insert'):
           counterI+=1

    for l in listsum:
        ltoint=float(l)
        sum+=ltoint


def main():
    mainCsv = pd.DataFrame(columns=['RunningTime', 'A', 'B', 'C', 'SumOfRunning'])
    df = pd.read_csv('DataFrame1.csv')

    df['QueryType'] = df['Query'].apply(lambda  x: get_query_type(x))
    df = df[df.QueryType > -1]
    df = df[['StartTime', 'QueryType', 'RunTime']]
    hours = df['StartTime'].unique()
    for hour in hours:
        new_df = pd.DataFrame()
        new_df = df.loc[df['StartTime'] == hour]
        mainCsv = ortal_main(mainCsv,hour, new_df)
        mainCsv.to_csv("mainCsv.csv", index=False)


def get_query_type(query):
    ret_val = -1
    cluster = query.split(" ")
    if (str(cluster[0]).lower() == 'select'):
        ret_val = 0
    if (str(cluster[0]).lower() == 'update'):
        ret_val = 1
    if (str(cluster[0]).lower() == 'insert'):
        ret_val = 2

    return ret_val

main()
