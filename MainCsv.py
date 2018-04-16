import powerSetFinder as psf;
import csv;
import pandas as pd;


df = pd.read_csv('DataFrame.csv', header=None)
list=[]

# TODO change
# startTime = df[2]
startTime = '12:00'
total = df[0]
sum=0
listsum=[]

for t in total:
    listsum.append(t)
listsum.remove('RunTime')

query = df[1]
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
# list.append(sum)

list.append([startTime,counterS,counterU,counterI,sum])


mainCsv = pd.DataFrame(columns=['RunningTime','A','B','C','SumOfRunning'])
mainCsv = mainCsv.append(pd.Series(['12:00',counterS,counterU,counterI,sum], index=['RunningTime','A','B','C','SumOfRunning']),ignore_index=True)


mainCsv.to_csv("mainCsv.csv")

