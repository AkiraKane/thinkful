
import weather_utils as wu

# Data set is already populated with Boston data

# Read dataset
content = wu.load_30_days()

# Pull out daily and hourly data
daily = wu.extract_daily_from_json(content)
hourly = wu.extract_hourly_from_json(content)

values = {
    'high_max': daily['temperatureMax'].max(),
    'low_max': daily['temperatureMax'].min(),
    'mean_max': daily['temperatureMax'].mean(),
    'median_max': daily['temperatureMax'].median(),
    'greatest_delta_max': daily['changeMax'].max(),
    'smallest_delta_max': daily['changeMax'].min(),

    'high_min': daily['temperatureMin'].max(),
    'low_min': daily['temperatureMin'].min(),
    'mean_min': daily['temperatureMin'].mean(),
    'median_min': daily['temperatureMin'].median(),
    'greatest_delta_min': daily['changeMin'].max(),
    'smallest_delta_min': daily['changeMin'].min(),
}
print "BOSTON WEATHER\n"
print "HIGHS\n" \
      "Highest high: {high_max}\n" \
      "Lowest high: {low_max}\n" \
      "Median high: {median_max}\n" \
      "Mean high: {mean_max}\n" \
      "Greatest change: {greatest_delta_max}\n" \
      "Smallest change: {smallest_delta_max}\n" \
      "\n" \
      "LOWS\n" \
      "Highest high: {high_min}\n" \
      "Lowest high: {low_min}\n" \
      "Median high: {median_min}\n" \
      "Mean high: {mean_min}\n" \
      "Greatest change: {greatest_delta_min}\n" \
      "Smallest change: {smallest_delta_min}\n".format(**values)
