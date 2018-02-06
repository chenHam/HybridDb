import json
import uuid

import sys

import time

import CassandraProvider
import Common
import MysqlProvider


def main(argv):
    with open('configurationFile') as f:
        config = json.load(f)
    uid = uuid.uuid4()
    dataBase = sys.argv[1]

    DBkind = argv

    provider = {}
    if argv == "SQL":
        provider = MysqlProvider.MysqlProvider()
    elif argv == "CQL":
        provider = CassandraProvider.CassandrsaProvider()


    #####

    tableNames = provider.getTableNames()

    for table in tableNames:
        columnNames = provider.getTableColumnNames(table)

        powerSet = Common.getColumnsPowerSet(columnNames)

        colsJoined = ', '.join(powerSet)

        print("cols: " + colsJoined)

        query = 'SELECT ' + colsJoined + ' FROM northwind.' + table + ';'

        print('query: ' + query)

        con = provider.openConnection()

        t0 = time.time()

        t0ToStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t0))

        provider.execQuery(query, con)

        t1 = time.time()

        ##insert quert results

        total = t1 - t0

        print("done with cols, time: " + str(total))

        totalToStr = str(total)
        uidToStr = str(uid)

        query1 = ir.insertResult(tableNameStr, colsJoined, totalToStr, t0ToStr, uidToStr, DBkind)
        cursor.execute(query1)
        conn.commit()
        closeConnection(conn)

    #####

main(sys.argv[1])


