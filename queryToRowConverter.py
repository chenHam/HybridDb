
# I got query, for example- select * from df where id=1
# The function should return list of two lists: the first list will incluse the eses objests of the select part, the second will include the where part
# The objects are:id, name,year,grapes,country,region,description,picture (total - 8)

def listOfObjectsToBinaryList(listToConvert,objectList):
    list=[]
    for x in range(0,len(objectList)):
        list.append(0)
    for l in listToConvert:
        list[objectList.index(l.strip())]=1
    return list

def queryToRowConverter(query,objectsList):
    # GET THE TABLE NAME
    tableNameList = []
    tableName=query.split('from')[1].split(' ')[1]
    tableNameList.append(tableName)

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
    finalList.append(tableNameList)
    finalList.append(convertedSelectList)
    finalList.append(convertedWhereList)
    print(finalList)
    return finalList

# RUN
objectsList=["id", "name","year","grapes","country","region","description","picture"]
queryToRowConverter("select * from df where id=3 AND  picture=null ",objectsList)