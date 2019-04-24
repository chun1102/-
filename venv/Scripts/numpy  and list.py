import numpy as np
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 20)
df = pd.read_csv('dataset/2014-1.csv')
array = df['passenger_count'].values
array = array * 10
df['passenger_count'] = array
print(df.head())

array1 = df.values
print(array1)
print(array1[:, 0])


# ls1 = [[1, 2, 3], [4, 5, 6]]
# ls2 = [[4, 5, 6], [7, 8, 9]]
#
# array1 = np.array(ls1)
# array2 = np.array(ls2)

'''print('array1:', array1, type(array1))
print('array2:', array2, type(array2))
print('維度:', array1.ndim)
print('形狀:', array1.shape)
print('數值類型:', array1.dtype)
print('數值類型:', array1.size)'''

# array1 = array1.astype('float')
# print(array1.dtype)

# array1 = array1 * 10
# ls3 = [[1, 2, 3], [4, 5, 6]]
# array3 = np.array(ls3)
# print('形狀:', array3.shape)
#
# array3 = array3.reshape(3, 2)
# print(array3)

'''array4 = np.zeros(shape=(2, 3))
array5 = np.ones(shape=(3, 4))
array6 = np.empty(shape=(5, 6))
array7 = np.arange(20, 10, -2)
print(array4)
print(array5)
print(array6)
print(array7)'''

# array3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# array4 = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# array3 = np.array(array3)
# array4 = np.array(array4)
# array5 = np.concatenate((array3, array4), axis=0)
# print(array5)