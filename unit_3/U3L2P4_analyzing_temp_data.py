
import weather_utils as wu

# Data set is already populated with Boston data

# Read dataset
content = wu.load_30_days()

# Pull out daily and hourly data
daily = wu.extract_daily_from_json(content)
hourly = wu.extract_hourly_from_json(content)


s = daily.sort(columns='apparentTemperatureMinTime',ascending=True)

print s['temperatureMax'].min()
print s['temperatureMax'].max()
print s['temperatureMax'].mean()
print s['temperatureMax'].median()

print s['temperatureMin'].min()
print s['temperatureMin'].max()
print s['temperatureMin'].mean()
print s['temperatureMin'].median()