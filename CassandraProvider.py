from cassandra.cluster import Cluster
import Common
from MysqlProvider import MysqlProvider


class CassandrsaProvider:

    mysqlProvider = {}

    def __init__(self):
        mysqlProvider = MysqlProvider()
        print("in cassasndra")

    def openConnection(self):
        ip = Common.getFromConfiguration("CQL", "host_ip")
        port = Common.getFromConfiguration("CQL", "port")
        cluster = Cluster([ip], port)
        conn = cluster.connect()
        return conn

    def closeConnection(con, self):
        con.close()

    def getTableNames(self):
        conn = self.openConnection()
        tableNames = []
        rows = conn.execute("select table_name from system_schema.tables where keyspace_name = '" + DB + "'")
        for row in rows:
            tableNames.append(row)
        self.closeConnection(conn)

        return tableNames

    def getTableColumnNames(tableName, self):
        conn = self.openConnection()
        query = "select column_name from system_schema.columns where table_name = '" + tableName + "'"
        rows = conn.execute(query)
        columnNames = []
        for row in rows:
            columnNames.append(row)
        self.closeConnection(conn)

        return columnNames

    def execQuery(con, query, self):
        con.execute(query)

    def insertResult(self, tableName ,cols ,timeAmount, startTime, processId):
        conn = self.mysqlProvider.openConnection()

        self.mysqlProvider.execQuery(conn, 'INSERT INTO Results (TableName, Columns, TimeAmount, Start_Time, Process_ID, db) VALUES (' "'" +
                                     tableName + "' ," + "'" + cols + "' ," + "'" + timeAmount + "' ," + "'" + startTime + "' ," + "'" + processId
                                     + "' ," + "CQL" ');')

        self.mysqlProvider.closeConnection(conn)




