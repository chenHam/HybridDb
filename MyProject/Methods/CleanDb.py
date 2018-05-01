import pymysql

def clean():
    print("----------start to clean db..----------")
    conn = pymysql.connect(host="193.106.55.134", port=3306, user='root', password='root', db='winecellar')
    cursor=conn.cursor()
    cursor.execute("truncate table  performance_schema.events_statements_history_long;")
    conn.close()
    print("----------finish to clean db..----------")

