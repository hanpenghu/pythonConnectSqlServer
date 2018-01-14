# -*- coding: UTF-8 -*-
import sys
# import pymssql
#尝试数据库连接
from code import *
from lianxi001Connect import *

conn = gc();
# print(conn==None);
cur=conn.cursor();
cur.execute('select top 7* from lian');
results=cur.fetchall()
for row in results:

      id= row[0]


      name=c(row[1])

      age = row[2]

      if(row[3]==None):
            idd=row[3]
      else:
            idd=c(row[3])

      print(id,",",age,",",name,",",idd)
cur.close();
conn.close();