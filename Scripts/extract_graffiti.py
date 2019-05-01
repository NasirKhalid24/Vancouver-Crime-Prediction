# The following script extracts graffiti data
import pandas as pd
import numpy as np

f = open('../Datasets/graffiti.kml', 'r')
content = f.readlines()

# SAMPLE COORDINATE: <coordinates>-123.113935739267,49.2613158916217,0.0</coordinates>

lats = []
longs = []
for i, line in enumerate(content):
        if '<coordinates>' in line:
                long = float(line[13:line.find(',')])
                lat = float(line[line.find(',')+1:line.rfind(',')])
                lats.append(lat)
                longs.append(long)

df = pd.DataFrame({'Latitude': lats, 'Longitude': longs})
df.to_csv('../Datasets/Graffiti.csv', index = None)