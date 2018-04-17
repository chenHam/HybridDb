import pymysql
import pandas as pd
import datetime


conn = pymysql.connect(host="193.106.55.134", port=3306, user='root', password='root', db='winecellar')
df = pd.DataFrame(columns=['StartTime','RunTime','Query'])

cursor = conn.cursor()
# cursor.execute("SELECT EVENT_ID, \
#                         TRUNCATE(TIMER_WAIT/1000000000000,6) as Duration,\
#                         SQL_TEXT\
#                 FROM performance_schema.events_statements_history_long\
#                 WHERE SQL_TEXT like '%wine%' "
#                "        and SQL_TEXT not like '%SQL_TEXT%'"
#                "        and SQL_TEXT like '%SELECT%'"
#                 )
cursor.execute("SELECT DATE_SUB(NOW(), INTERVAL (SELECT VARIABLE_VALUE \
               FROM performance_schema.global_status WHERE VARIABLE_NAME='UPTIME') - TIMER_START*10e-13 second)\
               AS `start_time`,\
                ROUND(timer_wait*10E-10, 3) AS `wait in (ms)`,\
               sql_text\
               FROM performance_schema.events_statements_history_long\
               WHERE SQL_TEXT like '%wine%' and SQL_TEXT not like '%SQL_TEXT%'")

results = cursor.fetchall()
list = []
listTime=[]
listHour=[]
i=0
for r in results:
    list.append(r)


df = pd.DataFrame(list,columns=['StartTime','RunTime','Query'])
df.to_csv("DataFrame1.csv")

print(df)
conn.close()


