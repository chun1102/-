import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_column', 20)
df = pd.read_json('df.json')
print(df.head())
print(df['speed'])
#rint(df.loc[:, ['speed']])
#print(df.loc[5:7])
#print(df.loc[[5]])
#print(df.loc[[8], ['speed']])
df['test'] = 0
#print(df.head())
print(df[df['datacollecttime'] == '2018-11-01 00:00:00'])
con1 = df['speed'] >= 80
con2 = df['speed'] <= 100
print(df[con1 & con2])
con3 = df['speed'].isin([80, 90, 100])
print(df[con3])
print(df.sort_values(by='speed', ascending=False))
speed_max = df['speed'].max()
con4 = df['speed'] == speed_max
print(df[con4])
con5 = df['volume'] >= 60
con6 = df['volume'] <= 180
print(df[con5 & con6])
print(df[df['datacollecttime'] == '2018-11-01 04:00:00'])
con7 = df['laneoccupy'] >= 2.0
print(df[con7])
df_sort = df.sort_values(by='volume',  ascending=False)
print(df_sort.head(5))