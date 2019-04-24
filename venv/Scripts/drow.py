import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataset/2014-1.csv')
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

df['date'] = df['pickup_datetime'].dt.date
# print(df.head())

date_group = df.groupby('date')
print(date_group.size())
# date_group.size().plot()
#plt.show()

df['day of week'] = df['pickup_datetime'].dt.dayofweek
# Monday = 0, Sunday = 6

day_of_week_group = df.groupby('day of week')
day_of_week_group.size()
# day_of_week_group.size().plot()
# plt.show()
#
# df['hour'] = df['pickup_datetime'].dt.hour
hour_group = df.groupby('hour')
# hour_group.size()
# hour_group.size().plot()
# plt.show()
gtoup_mean = hour_group.mean()
print(group_mean.head())
# avg_of_distance_and_rate.index.value = group_mean[['t']]
# sns.catplot(data=avg_of_distance_and_rate,
#             x=avg_of_distance_and_rate.index.value,
#             y='rate_code', color='gray')
# plt.show()