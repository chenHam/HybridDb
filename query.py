import pymysql
import pandas as pd
import random
import MysqlProvider
import powerSetFinder as psf
import random

conn = pymysql.connect(host="193.106.55.134", port=3306, user='root', password='root', db='winecellar')

cursor = conn.cursor()
cursor.execute("select Column_name\
                from INFORMATION_SCHEMA.COLUMNS\
                where TABLE_NAME='wine'")
results = cursor.fetchall()
res = [item[0] for item in results]
powerSet = psf.listToPowerset(res)
for col in powerSet:
    colsJoined = ', '.join(col)
    query = 'SELECT ' + colsJoined + ' FROM wine'
    cursor.execute(query)
    results = cursor.fetchall()
    #print(results)

cursor.execute("SELECT MAX(ID) FROM wine")
results = cursor.fetchall()
res = [item[0] for item in results]
toInt = [int(i) for i in res]
max = toInt[0]
r = random.randint(1, max)
rToStr = str(r)
query = "SELECT id FROM wine WHERE id >= " + rToStr + " ORDER BY ID LIMIT 1"
cursor.execute(query)
results = cursor.fetchall()
print(results)

cursor.execute("SELECT * FROM wine ORDER BY RAND() LIMIT 1")
results = cursor.fetchall()
print(results)

cursor.execute("SELECT * FROM wine WHERE country = 'USA' ORDER BY RAND() LIMIT 1")
results = cursor.fetchall()
print(results)

cursor.execute("UPDATE wine\
                SET name = 'cabernet sauvignon'\
                WHERE id = RAND()")
conn.commit()

cursor.execute("UPDATE wine\
                SET year = '2007'\
                WHERE year = '2009' ")
conn.commit()

cursor.execute("UPDATE wine\
                SET country = 'USA'\
                WHERE region = 'California' or region = 'Washington' ")
conn.commit()

# cursor.execute("INSERT INTO wine (name, year, Country, grapes, region, description, id)\
#                 VALUES ('Cabernet Sauvignon', '2012', 'Israel', 'red wine grape varieties', 'A', '', 13)")
# conn.commit()

# cursor.execute("DELETE FROM wine\
#                 WHERE year BETWEEN 1900 AND 1999' ")
# conn.commit()







conn.close()
