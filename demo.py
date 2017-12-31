import pymysql;
#import cassandra;
import time;
import json;

import sys;


import powerSetFinder as psf;
import insertResult as ir;
import uuid;

# -----------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------


def openConnection(dataBase):
    ip = getFromConfiguration(dataBase, "host_ip")
    port = getFromConfiguration(dataBase, "port")
    user = getFromConfiguration(dataBase, "user")
    password = getFromConfiguration(dataBase, "password")
    db = getFromConfiguration(dataBase, "db")
    if dataBase == "SQL":
        conn = pymysql.connect(host=ip, port=port, user=user, password=password, db=db)
    #if dataBase == "CQL":
        #conn = cql.connect(host=ip, port=port, user=user, password=password, db=db)
    return conn


def closeConnection(con):
    con.close()


def getFromConfiguration(name, var):
    try:
        return config.get(name)[var]
    except Exception as e:
        e1 = str(e)
        print("Exception: " + e1)
        return ""


def getTableNames(DB):
    conn = openConnection(DB)
    cursor = conn.cursor()
    cursor.execute("select table_name from information_schema.tables where table_schema = 'northwind'")
    tableNames = cursor.fetchall()
    closeConnection(conn)

    return tableNames


def getTableColumnNames(tableName):
    conn = openConnection(dataBase)
    cursor = conn.cursor()
    query = "select column_name from information_schema.columns where table_name = '" + tableName + "'"
    cursor.execute(query)
    columns = cursor.fetchall()
    closeConnection(conn)

    return columns


def getColumnsPowerSet(columns):
    return psf.listToPowerset(columns)


def getQueryTime(query):
    con = openConnection(dataBase)
    cursor = con.cursor()
    t0 = time.time()
    cursor.execute(query)
    t1 = time.time()
    closeConnection(con)

    total = t1 - t0
    return total


# -----------------------------------------------------
# THE MAIN PROGRAM
# -----------------------------------------------------
def main(argv):
    DBkind=argv
    conn = openConnection(DBkind)
    cursor = conn.cursor()
    cursor.execute("select table_name from information_schema.tables where table_schema = 'northwind'")
    tableNames = cursor.fetchall()
    closeConnection(conn)

    for tableName in tableNames:
        tableNameStr = tableName[0]
        print(tableNameStr)

        conn = openConnection(DBkind)
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
                # uid = uuid.uuid3(uuid.NAMESPACE_OID,query)

                conn = openConnection(DBkind)
                cursor = conn.cursor()
                t0 = time.time()
                t0ToStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t0))
                cursor.execute(query)
                t1 = time.time()

                total = t1 - t0
                print("done with cols, time: " + str(total))

                totalToStr = str(total)
                uidToStr = str(uid)
                query1 = ir.insertResult(tableNameStr, colsJoined, totalToStr, t0ToStr, uidToStr, DBkind)
                cursor.execute(query1)
                conn.commit()
                closeConnection(conn)

            except Exception as e:
                e1 = str(e)
                print("exception: " + e1)

                print('')

        print("done with current table")
    print ("done")
    print ('')


# -----------------------------------------------------
# RUN THIS
# -----------------------------------------------------

#new cassandra driver usage: https://datastax.github.io/python-driver/getting_started.html

with open('configurationFile') as f:
    config = json.load(f)
uid = uuid.uuid4()
dataBase=sys.argv[1]

#print (cassandra.__version__)

main(dataBase)