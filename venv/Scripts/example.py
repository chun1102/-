import numpy as np
import pandas as pd
x = input("請輸入X")
y = input('請輸入Y')
x = int(x)
y = int(y)
array0 = np.zeros(shape=(x,y))
array = np.arange(x)
header = array
for i in range(y):
    array0[i] = array[i] * array
data = pd.DataFrame(array0, columns=header)
print(data)
