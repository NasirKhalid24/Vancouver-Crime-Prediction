import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

df_crimes = pd.read_csv('../Datasets/final_crime.csv')
df_crimes = df_crimes[['Latitude', 'Longitude']] 
df_crimes = np.array(df_crimes)

df_graffiti = pd.read_csv('../Datasets/Graffiti.csv')
df_graffiti = df_graffiti[['Latitude', 'Longitude']] 
df_graffiti = np.array(df_graffiti)

distance_to_graffiti = []
print(df_crimes)
# convert decimal degrees to radians 
df_crimes, df_graffiti = map(radians, [df_crimes, df_graffiti])
print(df_crimes)
# for crime in df_crimes:
#     if crime[0] != 0:
#         distance = 100000000
#         for graffiti in df_graffiti:
#             x = haversine(crime[0], crime[1], graffiti[0],  graffiti[1])
#             if x < distance:
#                 distance = x
#         distance_to_graffiti.append(distance)
#     else:
#         distance_to_graffiti.append(-1)

# print("FINISHED LOOP!")

# final_crime = pd.read_csv('../Datasets/final_crime.csv')
# final_crime['Graffiti'] = distance_to_graffiti
# final_crime.to_csv('../Datasets/final_crime.csv', index=False)