import pymysql;

def insertResult(name ,cols ,time, start, processId):
    query1 = 'INSERT INTO Results (TableName, Columns, TimeAmount, Start_Time, Process_ID) VALUES (' "'" + name + "' ," + "'" + cols + "' ," + "'" + time + "' ," + "'" + start + "' ," + "'" + processId + "'"');'
    return query1


