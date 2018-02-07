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
tableColumnsNames=["tableName","select_id", "select_name","select_year","select_grapes","select_country","select_region","select_description","select_picture","where_id", "where_name","where_year","where_grapes","where_country","where_region","where_description","where_picture","runningTime"]
objectsList=["id", "name","year","grapes","country","region","description","picture"]
#TODO :: here I get the df from csv. if I would get him as df just replace the row.
df = pd.read_csv('tableOfQueriesAndTimes.csv')
data = []
for i in df.values:
    reasult=queryToRowConverter(i[0],objectsList)
    reasult.append(i[1])
    data.append(reasult)
finalDf=pd.DataFrame(data,columns=tableColumnsNames)
# CONVERT THE FEATUERS TO NUMERIC: to translte back: le.transform(THE FETCHER NAME)
translate = lambda row: wde.transform([row])[0]
wde = preprocessing.LabelEncoder()
wde.fit(finalDf['tableName'])
finalDf['tableName'] = finalDf['tableName'].apply(translate)
finalDf.to_csv("formattedQueries.csv")
# PRINT DENDROGRAM
Z = hierarchy.linkage(finalDf, 'ward')
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=5, labels=finalDf.index)
# SHOW CLUSTERS
belongs= fcluster(Z,5,criterion='maxclust')
print(belongs)
plt.show()

