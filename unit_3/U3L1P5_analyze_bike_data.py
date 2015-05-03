__author__ = 'jriley'
# Analyze an hour of data, shows which station had the max traffic
# https://courses.thinkful.com/data-001v2/project/3.1.5

import bike_utils as utils
from collections import defaultdict
import matplotlib.pyplot as plt

# read and scrub our data
data = utils.fetch_availability_data()
utils.add_bike_delta(data)

# calculate activity levels

activity = defaultdict(int)

# JR there's probably a dictionary comprehension or something more Pythonic to do this
for index,item in data.iterrows():
    activity[item['station_id']] += abs(int(item['change']))

    '''
    # JR - plt.bar doesn't like string names instead of station IDs
    # This:
    activity[item['stationName']] += abs(int(item['change']))

    # produces a stack trace that ends with :
    File "/Users/jriley/anaconda/lib/python2.7/site-packages/matplotlib/transforms.py", line 829, in from_bounds
        return Bbox.from_extents(x0, y0, x0 + width, y0 + height)
    TypeError: coercing to Unicode: need string or buffer, float found

    How would you show station names?
    '''

# Show our results
plt.xlabel('Station ID')
plt.ylabel('# bikes coming and going')
plt.bar( activity.keys(), activity.values())
plt.show()
