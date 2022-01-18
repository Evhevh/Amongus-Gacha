# 1/14/22 avh - This module contains common and shared database code used by other data_service modules
import sqlite3
from sqlite3 import Error


def get_connection():
    """ create a database connection to the SQLite database
    :return: Connection object or None
    """
    db_file = r"D:\!Pycharmprojects\db\amongusgachagame.sqlite3"
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
