__author__ = 'me'

import datetime
import json
import requests
import sqlite3 as lite

cities = {"Atlanta": (33.762909,-84.422675),
          "Austin": (30.303936,-97.754355),
          "Boston": (42.331960,-71.020173),
          "Chicago": (41.837551,-87.681844),
          "Cleveland": (41.478462,-81.679435)
          }

# *========= FORECAST.IO ===========* #

def load_api_key():
    with open('forecastio_api.key', 'r') as fp:
        key = (fp.readlines()).strip()
    return key

def request_data(lat_lon, timestamp):
    server = 'https://api.forecast.io/forecast'
    key = load_api_key()

    url = '%s/%s/%f,%f,%d' % (server, key, lat_lon[0], lat_lon[1],timestamp)
    r = requests.get(url)
    if r.status_code != 200:
        print ("WARNING: received a status code of ", r.status_code, " from ", url)
        return {}
    return r.json()


# *================ DATA CACHE ========* #

def cache_filepath(lat_lon, timestamp):
    return "./data/%f,%f,%d.json" % (lat_lon[0], lat_lon[1], timestamp)


def get_cached_response(lat_lon, timestamp):
    try:
        with open(cache_filepath(lat_lon, timestamp), 'r') as fd:
            return json.load(fd, encoding='utf-8')
    except IOError:
        print "No such file"
        return None

def write_to_cache(obj, lat_lon, timestamp):
    try:
        with open(cache_filepath(lat_lon, timestamp), 'w') as fd:
            fd.write( json.dumps(obj, encoding='utf-8'))
    except IOError:
        print "Could not write file"
        return None

# *============== GENERAL =========* #

def get_unix_timestamp(offset):
    when = datetime.datetime.utcnow()
    #if offset > 0:
    when = when - datetime.timedelta(days=offset,
                                     hours=when.hour,
                                     minutes=when.minute,
                                     seconds=when.second,
                                     microseconds=when.microsecond)
    epoch_seconds = (when - datetime.datetime(1970,1,1)).total_seconds()
    return int(epoch_seconds)


def fetch_weather_data(lat_lon, offset):
    timestamp = get_unix_timestamp(offset)
    obj = get_cached_response(lat_lon, timestamp)
    if not obj:
        print "Fetching data the hard way"
        obj = request_data(lat_lon, timestamp)
        write_to_cache(obj, lat_lon, timestamp)
    return obj



def populate_30_days():
    for days_past in range(0,30):
        data = fetch_weather_data(cities['Boston'], days_past)
        #add max_temp to database


#* ============= DATABASE ==================* #

db_name = 'weather.db'

def db_connect():
    '''
    Connect to our database.
    :return: a connection
    '''

    return lite.connect(db_name)


def create_tables(con):
    '''
    One-time table creation
    :param con: a database connection
    :return: None
    '''
    with con:
        con.cursor().execute('CREATE TABLE cities '\
                             '(id INT PRIMARY KEY, '\
                             'city TEXT,  '\
                             'latitude NUMERIC, '\
                             'longitude NUMERIC)')

        con.cursor().execute('CREATE TABLE temperature '\
                             '(id INT PRIMARY KEY, '\
                             'timestamp INT, '\
                             'max INT, '\
                             'min INT,'
                             'city TEXT )')


def insert_data(city, timestamp, max, min, con):
    '''
    Load our station profile table
    :param data: a list of station profile dictionaries
    :param con: database connection
    :return:
    '''
    sql = 'INSERT INTO temperature ( city, timestamp, max, min) ' \
          'VALUES (?,?,?,?)'


    #populate values in the database
    with con:
        cur = con.cursor()
        for resut in data:
            cur.execute(sql,(city, timestamp, max, min))


def fetch_availability_data():
    con = db_connect()

    # JR a good coder would query the stations table for station name
    # at report time instead of selecting it on every row.  Oh well.
    query = 'SELECT a.station_id, a.bikes, a.timestamp, s.stationName ' \
            'FROM availability a, stations s ' \
            'WHERE a.station_id = s.id ' \
            'ORDER BY a.station_id, a.timestamp ASC'

    return pd.read_sql_query(query, con)




#* ============= MAIN ======================* #

if __name__ == '__main__':
    print('Populating data...')
    populate_30_days()