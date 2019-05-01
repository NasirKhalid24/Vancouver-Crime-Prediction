import pandas as pd
import numpy as np
from os import path 

basepath = path.dirname(__file__)

finalcrimepath = path.abspath(path.join(basepath, "..","Datasets", "final_crime.csv"))
graffitipath = path.abspath(path.join(basepath, "..","Datasets", "Graffiti.csv"))

df_crimes = pd.read_csv(finalcrimepath)
df_crimes = df_crimes[['Latitude', 'Longitude']] 
df_crimes = np.array(df_crimes)
df_crimes = np.radians(df_crimes)

df_graffiti = pd.read_csv(graffitipath)
df_graffiti = df_graffiti[['Latitude', 'Longitude']] 
df_graffiti = np.array(df_graffiti)
df_graffiti = np.radians(df_graffiti)

distance_to_graffiti = []
r = 6371
total = len(df_crimes[:, 0])

for i, crime in enumerate(df_crimes):
    if crime[0] != 0:
        x =  df_graffiti - crime
        a = np.square(np.sin(x[:, 0]/2.0)) + np.cos(crime[0]) * np.cos(df_graffiti[:, 0]) * np.square(np.sin(x[:, 1]/2.0))
        c = 2 * np.arcsin(np.sqrt(a)) 
        distance_to_graffiti.append(np.amin(c)*r)
    else:
        distance_to_graffiti.append(-1)
    if ((i/total)*100)%25 == 0:
        print("% Done = " +str(((i/total)*100)))

print("FINISHED LOOP!")

final_crime = pd.read_csv(finalcrimepath)
final_crime['Graffiti'] = distance_to_graffiti
final_crime.to_csv(finalcrimepath, index=False)