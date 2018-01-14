#coding:UTF-8
import pymssql
#尝试数据库连接
from code import *

conn = pymssql.connect(host="127.0.0.1:1433",user="sa",password="root", database="lianxi001");
# print(conn==None);
cur=conn.cursor();
cur.execute('select top 5 * from lian');
results=cur.fetchall()
for row in results:
      id = row[0]
      name =getCode(row[1],"GBK")
      age = row[2]
      print(id,",",age,",",name)
cur.close();
conn.close();