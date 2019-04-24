import pandas as pd
import  datetime
import os
import numpy as np
org_data = pd.read_csv('nyc_taxi_dirty_data.csv')

# df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
header = ['pickup_datetime', 'passenger_count', 'pickup_longitude', 'pickup_latitude']
data_uni = org_data['Index of Data'].unique()

#result = pd.DataFrame(columns=header)
result = np.array([])
array = org_data.values
for i in range(50):
    con = array[:, 1] == i
    select_dataframe = array[con]
    array_values = select_dataframe[:, 0]
    array_values =  array_values.reshape(1, 4)
    if result.size == 0:
        result = array_values
    else:
        result = np.concatenate((result, array_values), axis=1)
    # print(array_values)
    print(result)
    org_data = pd.DataFrame(result, columns=header)
    #result = result.append(df, ignore_index=False)



# df.sort_values(by= 'Index of Data',ascending=True)
# print(df)

