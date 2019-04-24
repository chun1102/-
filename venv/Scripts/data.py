import pandas as pd
import datetime
import os

df = pd.read_csv('nyc_taxi_sample.csv')
df.describe()

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
datetime_value = df['pickup_datetime'].apply(lambda i: i.strftime('%Y-%m'))
# print(datetime_value)
# 取得各日期
datetime_uni = datetime_value.unique()
# print(datetime_uni)

dir = 'dataset'
# os.makedirs(dir)

for item in datetime_uni:
  time = datetime.datetime.strptime(item, '%Y-%m')
  year = time.year
  month = time.month
  con = df['pickup_datetime'].dt.year == year
  con1 = df['pickup_datetime'].dt.month == month
  select = df[con & con1]

  filename = dir + '/' + str(year) + '-' + str(month) + '.csv'

  select.to_csv(filename, encoding='utf-8', index=False)