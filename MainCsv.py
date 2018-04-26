import pandas as pd;
from datetime import date, datetime, timedelta




def ortal_main(mainCsv,hour,df,range,i):

    # print(df)
    # startTime = hour
    a=str(range[i])[:19]
    b=str(range[i+1])[:19]
    startTime = a+"-"+b
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
    mainCsv = pd.DataFrame(columns=['RunningTime', 'A', 'B', 'C', 'SumOfRunning'])
    df = pd.read_csv('DataFrame_3001_fat_queries.csv')

    df['QueryType'] = df['Query'].apply(lambda  x: get_query_type(x))
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
       range = date_range(a, b, 10, 'seconds')

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
            mainCsv.to_csv("mainCsv-fat-1.csv", index=False)
            i += 1


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

main()
