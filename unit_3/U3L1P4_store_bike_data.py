__author__ = 'jriley'

'''
Challenge
Now that the tables have been created, create a script
based on the code you've written so far that downloads the data,
parses the result, and then uploads the data to the database.

The code then needs to sleep for a minute and then perform the same task.
Find a way to make this happen in your code.

The code only needs to run for an hour. If it's sleeping every minute,
the code only needs to loop 60 times. Find a way of doing this.
'''

import bike_utils as utils
import time

# Run this once
# utils.init_db()

for tick in range(5):
    print ("Import #", tick)
    utils.update_data()
    time.sleep(60)
