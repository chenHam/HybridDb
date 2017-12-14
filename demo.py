import pymysql;
import time;
import powerSetFinder as psf;
conn = pymysql.connect(host='193.106.55.134', port=3306, user='root', password='root', db='northwind')

cursor = conn.cursor()

cursor.execute("SHOW TABLES")

for (table_name,) in cursor:
        print(table_name)
        cursor.execute('SELECT * FROM northwind.'+table_name+';')
        columns = [i[0] for i in cursor.description]
        powerset = psf.listToPowerset(columns)

        for (ps) in powerset:
            cols = ', '.join(ps)
            query = 'SELECT ' + cols + ' FROM northwind.' + table_name + ';'

            t0 = time.time()
            cursor.execute(query)
            t1 = time.time()

            total = t1 - t0
            print('')
            #OrtalCode

print ('')