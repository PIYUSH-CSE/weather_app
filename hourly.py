# HOURLY FORECAST

import pandas as pd


def table(data):
    hourly_data = data['forecast']['forecastday'][0]['hour']

    df = pd.DataFrame(hourly_data)
    lst = df['time'].to_numpy()
    j = 0
    for i in lst:
        lst[j] = i[11:]
        j += 1
    l = []
    for i in lst:
        hour = int(i.split(':')[0])
        if hour == 0:
            timee = '12 AM'
        elif hour < 12:
            timee = str(hour) + ' AM'
        elif hour > 12:
            hour -= 12
            timee = str(hour) + ' PM'
        else:
            timee = str(hour) + ' PM'
        l.append(timee)
    df['time'] = l
    condition = []
    icons = []
    for i in range(len(df)):
        condition.append(data['forecast']['forecastday'][0]['hour'][i]['condition'])
        icons.append('https:' + str(data['forecast']['forecastday'][0]['hour'][i]['condition']['icon']))
    df1 = pd.DataFrame(condition)
    result = pd.concat([df, df1], axis=1, join='inner')
    result.drop(
        ['condition', 'time_epoch', 'code', 'uv', 'icon', 'temp_f', 'feelslike_f', 'will_it_rain', 'chance_of_rain',
         'will_it_snow', 'chance_of_snow', 'gust_kph', 'gust_mph', 'vis_miles', 'vis_km', 'dewpoint_f', 'heatindex_f',
         'windchill_f', 'precip_in', 'precip_mm', 'pressure_in', 'wind_degree', 'wind_mph', 'cloud', 'is_day',
         'wind_kph', 'wind_dir', 'pressure_mb', 'humidity', 'feelslike_c', 'windchill_c', 'heatindex_c', 'dewpoint_c'],
        axis=1, inplace=True)
    result['icons'] = icons
    result.set_axis(['Time', 'Temp', 'Condition', 'Icon'], axis='columns', inplace=True)
    return result
