import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')
with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print( "SQLITE version %s" % data)

    cur.execute("SELECT * FROM weather")
    rows = cur.fetchall()
    df = pd.DataFrame(rows)

    for colname in [desc[0] for desc in cur.description]:
        print colname






