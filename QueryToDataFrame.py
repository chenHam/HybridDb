import pymysql
import pandas as pd


conn = pymysql.connect(host="193.106.55.134", port=3306, user='root', password='root', db='winecellar')

cursor = conn.cursor()
cursor.execute("SELECT EVENT_ID, \
                        TRUNCATE(TIMER_WAIT/1000000000000,6) as Duration,\
                        SQL_TEXT\
                FROM performance_schema.events_statements_history_long\
                WHERE SQL_TEXT like '%wine%' "
               "        and SQL_TEXT not like '%SQL_TEXT%'"
               "        and SQL_TEXT like '%SELECT%'"
                )
results = cursor.fetchall()
list = []
for r in results:
    print(r)
    list.append(r)

cols = ['RunTime', 'Query']
df = pd.DataFrame(list, columns=['x','RunTime','Query'])
del df['x']

df.to_csv("DataFrame.csv")

print(df)
conn.close()


