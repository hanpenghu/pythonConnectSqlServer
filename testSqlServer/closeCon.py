# -*- coding: UTF-8 -*-

def closeCom(con,course):
    if(con!=None):
        con.commit()
        con.close()
    if (course != None):
        course.close()