import numpy as np
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 20)
df = pd.read_csv('iris123.csv')

data_lengh = df['sepal length (cm)'].values
data_lengh_mean = data_lengh.mean()
data_lengh_std = np.std(data_lengh)
data_lengh = (data_lengh-data_lengh_mean)/(data_lengh_std)
df['sepal length (cm)'] = data_lengh
print(df.head())
# data_width = df['sepal width (cm)'].values
# data_width_max = max(data_width)
# data_width_min = min(data_width)
#
# data_petal_length = df['petal length (cm)'].values
# data_petal_length_max = max(data_petal_length)
# data_petal_length_min = min(data_petal_length)
#
# data_petal_width = df['petal width (cm)'].values
# data_petal_width_max = max(data_petal_width)
# data_petal_width_min = min(data_petal_width)

# for i in range(50):
#     data_lengh[i] = (data_lengh[i] - data_lengh_min)/(data_lengh_max - data_lengh_min)
# data_lengh = (data_lengh- data_lengh_min)/(data_lengh_max - data_lengh_min)
# data_width = (data_width- data_width_min)/(data_width_max - data_width_min)
# data_petal_length = (data_petal_length- data_petal_length_min)/(data_petal_length_max - data_petal_length_min)
# data_petal_width = (data_petal_width- data_petal_width_min)/(data_petal_width_max - data_petal_width_min)

df['sepal length (cm)'] = data_lengh
# df['sepal width (cm)'] = data_width
# df['petal length (cm)'] = data_petal_length
# df['petal width (cm)'] = data_petal_width
print(df.head())