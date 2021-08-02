# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlite3
from sqlite3 import Error
import numpy as np


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn
def create_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS test '
              '(id INTEGER PRIMARY KEY, uniformi INTEGER, normali5 INTEGER, normali20 INTEGER, '
              'uniformf FLOAT, normalf5 FLOAT, normalf20 FLOAT)')

def insert_randoms(c):
    c.execute('SELECT count(*) from test;')
    size = c.fetchone()[0]
    for i in range(size, size + 400000):
        uniformi = np.random.randint(-100, 100)
        normali5 = round(np.random.normal(0,5))
        normali20 = round(np.random.normal(0,20))
        uniformf = np.random.uniform(-100, 100)
        normalf5 = np.random.normal(0,5)
        normalf20 = np.random.normal(0,20)

        r = c.execute('INSERT INTO test (id, uniformi, normali5, normali20, uniformf, normalf5, normalf20) VALUES (?,?,?,?,?,?,?);',
                      (i, uniformi, normali5, normali20, uniformf, normalf5, normalf20))



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    conn = create_connection('../dbfile.db')
    c = conn.cursor()
    create_table(c)
    insert_randoms(c)
    conn.commit()
    if conn:
        conn.close()