# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:22:39 2019

@author: seiic
"""

import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("..\sqlite\club2019.db")
cur = conn.cursor()

sqlfiles = ["..\sqlite\entrytype.sql",
            "..\sqlite\shashu.sql",
            "..\sqlite\team.sql"]

for file in sqlfiles:
    fd = open(file, "r", encoding="utf-8")
    sql = fd.read()
    fd.close()
    
    sqlcommands = sql.split(';')
    
    for command in sqlcommands:
        try:
            cur.execute(command)
        except Error as e:
                print(e)
                conn.close()
                cur.close()
                
conn.close()
cur.close()
