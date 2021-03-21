# Copyright (c) 2019 Seiichi Ariga
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# -*- coding: utf-8 -*-

"""
Created on Sun Apr 28 13:17:46 2019

@author: Seiichi Ariga
"""

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        # TODO: 下はそのうち消す 2020/11
        # print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_connection("../sqlite/club2019.db")
