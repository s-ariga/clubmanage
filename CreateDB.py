# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:17:46 2019

@author: seiic
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection("..\sqlite\club2019.db")