import pymysql;

def insertResult(name ,cols ,time):
    query1 = 'INSERT INTO Results (TableName, Columns, TimeAmount) VALUES (' "'"+ name + "' ," + "'" + cols + "' ," + "'" + time + "'" ');'
    return query1


