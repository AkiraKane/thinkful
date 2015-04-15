import sqlite3 as lite
import pandas as pd


def load_data(cursor):
    for line in read_migration_file():
        cursor.execute(line)

def read_migration_file():
    with open('cities_and_weather.sql') as dump:
        for line in dump:
            yield line

def fetch_data(cursor):
    cursor.execute("SELECT c.* FROM cities c " +
                   "INNER JOIN weather w ON name = city "
                   "WHERE w.warm_month='July' " +
                   "ORDER BY c.name, c.state;")
    return cursor.fetchall()


if __name__ == '__main__':

    conn = lite.connect('challenge.db')

    with conn:
        cur = conn.cursor()
        load_data(cur)

        print( "The cities that are warmest in July are:")
        for row in fetch_data(cur):
            print("%s, %s" % (row[0], row[1]))





