import pandas as pd;
from datetime import date, datetime, timedelta
import os.path
import MyProject.Methods.dfToGraphs as gr


def ortal_main(mainCsv,hour,df,range,i):

    # print(df)
    # startTime = hour
    a=str(range[i])[:19]
    b=str(range[i+1])[:19]
    startTime = a+"-"+b
    total = df['RunTime'].sum()
    queries_type = df['QueryType']

    counterS1 = 0
    counterS2 = 0
    counterU = 0
    counterI = 0

    for type in queries_type:
        if type == 10:
            counterS1+=1
        if type == 20:
            counterS2+=1
        # if type == 1:
        #     counterU+=1
        # if type == 2:
        #     counterI+=1

    mainCsv = mainCsv.append(pd.Series([startTime, counterS1,counterS2, counterU, counterI, total], index=['RunningTime','A','B','C','D', 'SumOfRunning']),ignore_index=True)
    return mainCsv

# def test():
#     for t in total:
#         listsum.append(t)
#     listsum.remove('RunTime')
#
#     query = df[3]
#     listquery = []
#     for q in query:
#         listquery.append(q)
#     listquery.remove("Query")
#
#     counterS=0
#     counterU=0
#     counterI=0
#     for l in listquery:
#         cluster = l.split(" ")
#         if(str(cluster[0]).lower() == 'select'):
#             counterS+=1
#         if(str(cluster[0]).lower() == 'update'):
#             counterU+=1
#         if (str(cluster[0]).lower() == 'insert'):
#            counterI+=1
#
#     for l in listsum:
#         ltoint=float(l)
#         sum+=ltoint


def main():
    mainCsv = pd.DataFrame(columns=['RunningTime', 'A', 'B', 'C', 'D', 'SumOfRunning'])
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../FilesAndInputs/test.csv")
    df = pd.read_csv(path)

    df['QueryType'] = df['Query'].apply(lambda x: get_query_type(x))
    df = df[df.QueryType > -1]
    df = df[['StartTime', 'QueryType', 'RunTime']]
    hours = df['StartTime'].unique()

    size = len(hours)
    hours.sort()
    start_date = hours[0]
    a=datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S.%f")
    end_date = hours[size-1]
    b=datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S.%f")

    for dt in hours:
       range = date_range(a, b, 10, 'minutes')

    range_size = len(range)-1
    i=0
    # for hour in range:
    for hour in hours:
        if(i<range_size):
            new_df = pd.DataFrame()
            df['StartTime'] = pd.to_datetime(df['StartTime'])
            mask = (df['StartTime'] > range[i]) & (df['StartTime'] <= range[i+1])
            new_df = df.loc[mask]
            print(new_df)
            mainCsv = ortal_main(mainCsv,hour, new_df,range,i)
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../FilesAndInputs/testMINI.csv")
            mainCsv.to_csv(path, index=False)
            i += 1


def get_query_type(query):
    ret_val = -1
    cluster = query.split(" ")
    if (str(cluster[0]).lower() == 'select'):
        list=[]
        start_index = 'select'
        end_index = 'from'
        start_index = query.index(start_index)
        end_index = query.index(end_index)
        sublist = query[start_index:end_index].split(',')
        for l in sublist:
            list.append(l)
        print(list)
        size=len(list)
        if(size>7):
            ret_val = 10
        if(size<=7):
            ret_val = 20
    # if (str(cluster[0]).lower() == 'update'):
    #     ret_val = 1
    # if (str(cluster[0]).lower() == 'insert'):
    #     ret_val = 2

    return ret_val

def date_range(start_date, end_date, increment, period):
    result = []
    nxt = start_date
    delta = timedelta(**{period:increment})
    while nxt <= end_date:
        result.append(nxt)
        # d=str(delta)
        nxt += delta
        # nxt += d
    return result

# def date_between(date,range):
#     print(date)
#     a=datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
#     b=datetime.strptime(range[0], "%Y-%m-%d %H:%M:%S.%f")
#     if(date<b):
#         return

def Run():
    main()
    gr.main()