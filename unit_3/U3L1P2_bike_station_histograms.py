'''

1) Explore the other data variables. Are there any test stations?
How many stations are "In Service"? How many are "Not In Service"?
Any other interesting variables values that need to be accounted for?

2) What is the mean number of bikes in a dock? What is the median?
How does this change if we remove the stations that aren't in service?
'''


__author__ = 'jriley'
import requests

import matplotlib.pyplot as plt
import bike_utils as utils


df = utils.fetch_citibike_data()

# Explore
total_bikes = df['availableBikes'].sum()
max_available = df['availableBikes'].max()
total_docks = df['totalDocks'].sum()
max_docks = df['totalDocks'].sum()
min_docks = df['totalDocks'].min()

print "%d bikes are available" % (total_bikes)

# supposing that 1 dock == 1 bike, no extra parking spots
print "%d of %d bikes are in use" % ( max_docks - total_bikes, max_docks)


#liveStations = df[df['testStation'] == False]
testStations = df[df['testStation'] == True]
inServiceStations = df[df['statusKey'] == 1]
outOfServiceStations = df[df['statusKey'] != 1]
liveStations = inServiceStations[df['testStation'] == False]


print "Total number of test stations is ", len(df[df['testStation'] == True])
print "Total number of out of service stations is ", len(outOfServiceStations)
print "Out of service docks : %d and bikes: %d" % ( outOfServiceStations['totalDocks'].sum(),
    outOfServiceStations['availableBikes'].sum())

print "Total service available bikes: mean: %d median %d" % (df['availableBikes'].mean(), df['availableBikes'].median())
print "Live service available bikes: mean: %d median %d" % (liveStations['availableBikes'].mean(), liveStations['availableBikes'].median())
print "Out of service available bikes: mean: %d median %d" % (outOfServiceStations['availableBikes'].mean(), outOfServiceStations['availableBikes'].median())



# Plot available and docks

fig = plt.figure()

liveAvailable = fig.add_subplot(2,2,1)
plt.hist(liveStations['availableBikes'])
plt.xlabel('available bikes')
plt.ylabel('live stations')

liveDocks = fig.add_subplot(2,2,2)

# JR: changing the y ticks did nothing- ??
plt.yticks=10

plt.xlabel('total docks')
plt.ylabel('live stations')
plt.hist(liveStations['totalDocks'])



'''
# JR: plt gets cranky when there are 0 values - what do you do?

outOfService = fig.add_subplot(2,2,3)
plt.hist(outOfServiceStations['availableBikes'])
plt.xlabel('available bikes')
plt.ylabel('test stations')

outOfService = fig.add_subplot(2,2,4)
plt.hist(outOfServiceStations['totalDocks'])
plt.xlabel('total docks')
plt.ylabel('test stations')
'''


'''
f1 = fig.add_subplot(2,2,3)
plt.hist(df['availableBikes'])
plt.xlabel('available bikes')
plt.ylabel('a'' stations')

f2 = fig.add_subplot(2,2,4)
plt.hist(df['totalDocks'])
plt.xlabel('total docks')
plt.ylabel('all stations')

'''
plt.show()