import pymysql;
import time;
import powerSetFinder as psf;

def openConnection():
    conn = pymysql.connect(host='193.106.55.134', port=3306, user='root', password='root', db='northwind')

    return conn

def closeConnection(con):
    con.close()

def getTableNames():
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("select table_name from information_schema.tables where table_schema = 'northwind'")
    tableNames = cursor.fetchall()
    closeConnection(conn)

    return tableNames

def getTableColumnNames(tableName):

    conn = openConnection()
    cursor = conn.cursor()
    query = "select column_name from information_schema.columns where table_name = '" + tableName + "'"
    cursor.execute(query)
    columns = cursor.fetchall()
    closeConnection(conn)

    return columns

def getColumnsPowerSet(columns):
    return psf.listToPowerset(columns)

def getQueryTime(query):
    con = openConnection()
    cursor = con.cursor()
    t0 = time.time()
    cursor.execute(query)
    t1 = time.time()
    closeConnection(con)

    total = t1 - t0
    return total


conn = openConnection()
cursor = conn.cursor()
cursor.execute("select table_name from information_schema.tables where table_schema = 'northwind'")
tableNames = cursor.fetchall()
closeConnection(conn)

for tableName in tableNames:
    tableNameStr = tableName[0]
    print(tableNameStr)

    conn = openConnection()
    cursor = conn.cursor()
    query = "select column_name from information_schema.columns where table_name = '" + tableNameStr + "'"
    cursor.execute(query)
    closeConnection(conn)

    tableColumns = [i[0] for i in cursor.fetchall()]
    columnsPowerset = psf.listToPowerset(tableColumns)

    for (powerset) in columnsPowerset:
        try:
            colsJoined = ', '.join(powerset)
            print("cols: " + colsJoined)

            query = 'SELECT ' + colsJoined + ' FROM northwind.' + tableNameStr + ';'
            print('query: ' + query)

            con = openConnection()
            cursor = con.cursor()
            t0 = time.time()
            cursor.execute(query)
            t1 = time.time()
            closeConnection(con)

            total = t1 - t0
            print("done with cols, time: " + str(total))
        except Exception as e:
            print("exception: " + e)

            print('')
            # OrtalCode

    print("done with current table")
print ("done")
print ('')




