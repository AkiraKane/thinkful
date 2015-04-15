import sqlite3 as lite
import pandas as pd


def load_data(cursor):
    for line in read_migration_file():
        cursor.execute(line)

def read_migration_file():
    with open('cities_and_weather.sql') as dump:
        for line in dump:
            yield line




if __name__ == '__main__':

    conn = lite.connect('challenge.db')

    with conn:
        cur = conn.cursor()
        load_data(cur)





