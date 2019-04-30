import sqlite3
from sqlite3 import Error

db_file = '/cars/BlackJackSim/sqlitedb.db'

conn = sqlite3.connect(db_file)
c = conn.cursor()

def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS stats_table(unix REAL, p1_wins TEXT, palt_wins TEXT)')
    conn.commit()

def insertData(unix, p1, p2):
    c.execute('INSERT INTO stats_table VALUES(?, ?, ?)', (unix, p1, p2))
    conn.commit()