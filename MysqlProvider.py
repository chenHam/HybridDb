import pymysql
import Common

class MysqlProvider:
    def __init__(self):
        print("in mysql")

    def openConnection(self):
        ip = Common.getFromConfiguration("SQL", "host_ip")
        port = Common.getFromConfiguration("SQL", "port")
        user = Common.getFromConfiguration("SQL", "user")
        password = Common.getFromConfiguration("SQL", "password")
        db = Common.getFromConfiguration("SQL", "db")
        conn = pymysql.connect(host=ip, port=port, user=user, password=password, db=db)
        return conn

    def closeConnection(con, self):
        con.close()

    def getTableNames(self):
        conn = self.openConnection()
        cursor = conn.cursor()
        cursor.execute("select table_name from information_schema.tables where table_schema = 'northwind'")
        tableNames = cursor.fetchall()
        self.closeConnection(conn)

        return tableNames

    def getTableColumnNames(tableName, self):
        conn = self.openConnection()
        cursor = conn.cursor()
        query = "select column_name from information_schema.columns where table_name = '" + tableName + "'"
        cursor.execute(query)
        columns = cursor.fetchall()
        self.closeConnection(conn)

        return columns

    def execQuery(con, query, self):
        cursor = con.cursor()
        cursor.execute(query)