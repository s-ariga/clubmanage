"""
Seiichi Ariga <seiichi.ariga@gmail.com>
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
