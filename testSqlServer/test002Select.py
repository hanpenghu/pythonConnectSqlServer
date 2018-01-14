# -*- coding: UTF-8 -*-
from lianxi001Connect import *

from closeCon import *
sql1='''
 insert into lian (name1,age,idd)
 values('喊喊10',29,'水电费10')
'''

sql2="""
update lian set age =30 WHERE id = 11
"""

sql3="""
update lian set idd ='水电费1101' WHERE id = 11
"""
conn=gc()
c = conn.cursor()
c.execute(sql3)
closeCom(conn,c)



