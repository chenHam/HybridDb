import pandas as pd
import scipy

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
# tableColumnsNames=["tableName","select_id", "select_name0","select_year0","select_grapes0","select_country0","select_region0","select_description0","select_picture0","where_id", "where_name0","where_year0","where_grapes0","where_country0","where_region0","where_description0","where_picture0"
#                                             "select_name1","select_year1","select_grapes1","select_country1","select_region1","select_description1","select_picture1",            "where_name1","where_year1","where_grapes1","where_country1","where_region1","where_description1","where_picture1",
#                                             "select_name2","select_year2","select_grapes2","select_country2","select_region2","select_description2","select_picture2",            "where_name2","where_year2","where_grapes2","where_country2","where_region2","where_description2","where_picture2",
#                                             "select_name3","select_year3","select_grapes3","select_country3","select_region3","select_description3","select_picture3",            "where_name3","where_year3","where_grapes3","where_country3","where_region3","where_description3","where_picture3"
#                               ,"runningTime"]

tableColumnsNames=["tableName", "select_id", "select_name0","select_year0","select_grapes0","select_country0","select_region0","select_description0","select_picture0","where_id", "where_name0","where_year0","where_grapes0","where_country0","where_region0","where_description0","where_picture0"
                                            "select_name1","select_year1","select_grapes1","select_country1","select_region1","select_description1","select_picture1",            "where_name1","where_year1","where_grapes1","where_country1","where_region1","where_description1","where_picture1",
                                            "select_name2","select_year2","select_grapes2","select_country2","select_region2","select_description2","select_picture2",            "where_name2","where_year2","where_grapes2","where_country2","where_region2","where_description2","where_picture2",
                                            "select_name3","select_year3","select_grapes3","select_country3","select_region3","select_description3","select_picture3",            "where_name3","where_year3","where_grapes3","where_country3","where_region3","where_description3","where_picture3",
                              "abc","runningTime"]

#objectsList=["id", "name0","year0","grapes0","country0","region0","description0","picture0"]
objectsList=["id","name0","year0","grapes0","country0","region0","description0","picture0",
                 "name1", "year1", "grapes1", "country1", "region1", "description1", "picture1",
                 "name2", "year2", "grapes2", "country2", "region2", "description2", "picture2",
                 "name3", "year3", "grapes3", "country3", "region3", "description3", "picture3"
             ]
df = pd.read_csv('DataFrame2.csv')
del df['Unnamed: 0']
data = []
# Distinct the double queries. - OPTIONAL !!
# distinctQuery='select min(RunTime),Query from df group by Query'
# df=pysql(distinctQuery)
for i in df.values:
    i[2]=i[2].lower()
    if 'select' in i[2] and 'from' in i[2]:
        reasult=queryToRowConverter(i[2],objectsList)
        FAC=10000
        reasult.append(i[1]*FAC)
        data.append(reasult)
finalDf=pd.DataFrame(data,columns=tableColumnsNames)
#finalDf=pd.DataFrame(data)
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

