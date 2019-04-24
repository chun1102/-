import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_column', 20)
df1 = pd.read_json('df.json')
print(df1.head())
con1 = df['volume'] >= 60
con2 = df['volume'] <= 180
print(df[con1 & con2])
