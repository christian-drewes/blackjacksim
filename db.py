import sqlite3
import graph
from sqlite3 import Error

db_file = '/cars/BlackJackSim/sqlitedb.db'

conn = sqlite3.connect(db_file)
c = conn.cursor()

playerResult = 0

def createTable():
    c.execute("""CREATE TABLE IF NOT EXISTS 
        stats_table(
            unix REAL, 
            p1_wins TEXT, 
            palt_wins TEXT,
            d1_wins TEXT,
            dalt_wins TEXT
        )
    """)
    conn.commit()

def insertData(unix, p1, p2, d1, d2):
    c.execute('INSERT INTO stats_table VALUES(?, ?, ?, ?, ?)', (unix, p1, p2, d1, d2))
    conn.commit()

def countWins(player):
    str = f"""
        SELECT count({player})
        FROM stats_table
        WHERE {player}='win'
    """ 
    
    c.execute(str)
    return c.fetchone()[0]

def graphWins():
    graph.createGraph(
        countWins('p1_wins'),
        countWins('palt_wins'),
        countWins('d1_wins'),
        countWins('dalt_wins')
    )