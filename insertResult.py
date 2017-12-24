import pymysql;

def insertResult(name ,cols ,time, start, processId, dbkind):
    query1 = 'INSERT INTO Results (TableName, Columns, TimeAmount, Start_Time, Process_ID, db) VALUES (' "'" + name + "' ," + "'" + cols + "' ," + "'" + time + "' ," + "'" + start + "' ," + "'" + processId + "' ," + "'" + dbkind + "'" ');'
    return query1


