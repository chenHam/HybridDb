import pandas as pd
from scipy.cluster import hierarchy
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import fcluster
from sklearn import preprocessing

def listOfObjectsToBinaryList(listToConvert,objectList):
    list=[]
    for x in range(0,len(objectList)):
        list.append(0)
    for l in listToConvert:
        list[objectList.index(l.strip())]=1
    return list

def queryToRowConverter(query,objectsList):
    # GET THE TABLE NAME
    tableName=query.split('from')[1].split(' ')[1]

    # PARSE THE SELECT LIST OBJECTS
    selectObjectsList=query.split('from')[0].split('select')[1].split(',')
    if selectObjectsList[0].strip()=='*':
        convertedSelectList = listOfObjectsToBinaryList(objectsList, objectsList)
    else:
        convertedSelectList=listOfObjectsToBinaryList(selectObjectsList,objectsList)
    # PARSE THE WHERE LIST OBJECTS
    whereObjectsList=[]
    whereCheck=query.split(' ')
    if 'where' in whereCheck:
        ObjectsList=query.split('where')[1].split("AND")
        for l in ObjectsList:
            l=l.split('=')[0]
            whereObjectsList.append(l)
    convertedWhereList = listOfObjectsToBinaryList(whereObjectsList, objectsList)
    # CONVERTING INTO ONE LIST
    finalList = []
    finalList.append(tableName)
    finalList=finalList+convertedSelectList
    finalList=finalList+convertedWhereList
    return finalList

# RUN
import pandasql as pdsql

pysql = lambda q: pdsql.sqldf(q, globals())
tableColumnsNames=["tableName","select_id", "select_name","select_year","select_grapes","select_country","select_region","select_description","select_picture","where_id", "where_name","where_year","where_grapes","where_country","where_region","where_description","where_picture","runningTime"]
objectsList=["id", "name","year","grapes","country","region","description","picture"]
df = pd.read_csv('DataFrame.csv')
del df['Unnamed: 0']
data = []
# Distinct the double queries. - OPTIONAL !!
# distinctQuery='select min(RunTime),Query from df group by Query'
# df=pysql(distinctQuery)
for i in df.values:
    i[1]=i[1].lower()
    if 'select' in i[1] and 'from' in i[1]:
        reasult=queryToRowConverter(i[1],objectsList)
        FAC=10000
        reasult.append(i[0]*FAC)
        data.append(reasult)
finalDf=pd.DataFrame(data,columns=tableColumnsNames)
# CONVERT THE FEATUERS TO NUMERIC: to translte back: wde.transform(THE FETCHER NAME)
translate = lambda row: wde.transform([row])[0]
wde = preprocessing.LabelEncoder()
wde.fit(finalDf['tableName'])
finalDf['tableName'] = finalDf['tableName'].apply(translate)
finalDf.to_csv("formattedQueries.csv")
# PRINT DENDROGRAM
Z = hierarchy.linkage(finalDf, 'ward')
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=5, labels=finalDf.index) # to see queries replacw with df.values
# SHOW CLUSTERS
belongs= fcluster(Z,5,criterion='maxclust')
plt.show()