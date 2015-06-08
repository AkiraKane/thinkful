__author__ = 'me'

import datetime
import json
import requests
import sqlite3 as lite
import pandas as pd
import datetime
import forecast_io as forecast


CITIES = {"Atlanta": (33.762909,-84.422675),
          "Austin": (30.303936,-97.754355),
          "Boston": (42.331960,-71.020173),
          "Chicago": (41.837551,-87.681844),
          "Cleveland": (41.478462,-81.679435)
          }

DATA_DIR="./data/"

# *============= DATA MUNGING =========* #

## load the last 30 days of data.
## See note in __main__ at bottom about how boston_last_30.json was assembled
def load_30_days():
    datafile = DATA_DIR + "/boston_last_30.json"
    with open(datafile) as json_src:
        content = json.load(json_src)
        return content

def read_daily_json(content):
    for item in content:
        yield item['daily']['data'][0]



def extract_daily_from_json(content):
    dailies = []
    for item in content:
        i = item['daily']['data'][0]
        #i['date']= datetime.datetime.fromtimestamp(
        #        int(i['apparentTemperatureMinTime'])
        #    ).strftime('%Y-%m-%d')
        dailies.extend(item['daily']['data'])
    return pd.DataFrame(dailies)


def extract_hourly_from_json(content):
    hourlies = []
    for item in content:
        hourlies.extend(item['hourly']['data'])
    hourly_df = pd.DataFrame(hourlies)
    return hourly_df


# *================ CACHED DATA ========* #

def cache_filepath(lat_lon, timestamp):
    return DATA_DIR + "%f,%f,%d.json" % (lat_lon[0], lat_lon[1], timestamp)


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
        obj = forecast.request_data(lat_lon, timestamp)
        write_to_cache(obj, lat_lon, timestamp)
    return obj



def populate_30_days():
    for days_past in range(0,30):
        fetch_weather_data(CITIES['Boston'], days_past)


#* ============= MAIN ======================* #

if __name__ == '__main__':

    # Run the file directly to pull down the data files
    # This happens once, so __main__ is fine.
    print('Populating data...')
    populate_30_days()

    # The file boston_last_30.json was compiled manually from the daily json files
    # From the command line,
    #       cat 42*json >> boston_last_30.json
    # followed by correcting the json in emacs, to wit:
    #    * separating entries with commas
    #    * enclosing the json with an opening [ and ending ]
    # Possible in python, but much faster by hand

