import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.width', 200)
pd.set_option('display.max_column', 20)
df = pd.read_csv('dataset/2014-1.csv', encoding='utf-8')
print(df.head())
df['pick_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['hour'] = df['pick_datetime'].dt.hour
hour_group = df.groupby('hour')

'''rot是下排轉的角度'''
group_mean = hour_group.mean()
avg_of_distance_and_rate = group_mean[['trip_distance', 'rate_code']]
avg_of_distance_and_rate.plot(kind='scatter',
                              x='trip_distance',
                              y='rate_code')

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
ax1 = fig.add_subplot(2, 1, 2)
x_data = [x for x in range(24)]
ax.plot(x_data, group_mean['trip_distance'])
ax1.plot(x_data, group_mean['rate_code'])
plt.show()