import pandas as pd
import numpy as np
from os import path 

basepath = path.dirname(__file__)

finalcrimepath = path.abspath(path.join(basepath, "..","Datasets", "final_crime.csv"))
fountainpath = path.abspath(path.join(basepath, "..","Datasets", "drinking_fountains.csv"))

df_crimes = pd.read_csv(finalcrimepath)
df_crimes = df_crimes[['Latitude', 'Longitude']] 
df_crimes = np.array(df_crimes)
df_crimes = np.radians(df_crimes)

df_fountain = pd.read_csv(fountainpath)
df_fountain = df_fountain[['LATITUDE', 'LONGITUDE']] 
df_fountain = np.array(df_fountain)
df_fountain = np.radians(df_fountain)

distance_to_fountain = []
r = 6371
total = len(df_crimes[:, 0])

for i, crime in enumerate(df_crimes):
    if crime[0] != 0:
        x =  df_fountain - crime
        a = np.square(np.sin(x[:, 0]/2.0)) + np.cos(crime[0]) * np.cos(df_fountain[:, 0]) * np.square(np.sin(x[:, 1]/2.0))
        c = 2 * np.arcsin(np.sqrt(a)) 
        distance_to_fountain.append(np.amin(c)*r)
    else:
        distance_to_fountain.append(-1)
    if ((i/total)*100)%25 == 0:
        print("% Done = " +str(((i/total)*100)))

print("FINISHED LOOP!")

final_crime = pd.read_csv(finalcrimepath)
final_crime['Drinking_Fountain'] = distance_to_fountain
final_crime.to_csv(finalcrimepath, index=False)