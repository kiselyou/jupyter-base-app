import pymysql
import pandas

conn = pymysql.connect(
    host="localhost",
    port=int(3306),
    user="root",
    passwd="admin",
    db="ws",
    charset='utf8mb4')

def query(sql) :
    return pandas.read_sql_query(sql, conn)
