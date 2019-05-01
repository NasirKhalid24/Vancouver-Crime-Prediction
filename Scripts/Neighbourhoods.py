import pandas as pd
import numpy as np

file_path = '../Datasets/cov_localareas.csv'
file_path2 = '../Datasets/crime.csv'

df_localareas = pd.read_csv(file_path)
df_crimes = pd.read_csv(file_path2)

df_crimes = df_crimes[['Latitude', 'Longitude']] 

data = np.empty_like(df_crimes['Latitude'], dtype='<U24')

df_crimes = df_crimes.values
location_cords = df_localareas[['Latitude', 'Longitude']].values
addresses = df_localareas['NAME'].values

for n, i in enumerate(df_crimes):
    data[n] = addresses[np.argmin(np.sum(np.square(i-location_cords), axis=1))]
print(data)
print(data.shape)

final_crime = pd.read_csv(file_path2)
final_crime['Neighbourhood'] = data
final_crime.to_csv('../Datasets/final_crime.csv', index=False)