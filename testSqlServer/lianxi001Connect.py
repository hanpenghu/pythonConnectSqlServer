# -*- coding: UTF-8 -*-
import sys
import pymssql

def gc():
    conn = pymssql.connect(host="127.0.0.1:1433", user="sa", password="root", database="lianxi001")
    return conn