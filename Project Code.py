# Importing library to work with .csv files
import pandas as pd
import numpy as np

# final_crime contains all needed data & localareas contains information about neighbourhoods in Vancouver
file_path = 'final_crime.csv'

df = pd.read_csv(file_path,  error_bad_lines=False)
df = df[['YEAR','MONTH','DAY', 'Neighbourhood']] 

# Remove invalid date data
df = df[pd.isnull(df['Neighbourhood']) != pd.isnull(pd.NaT)]
print("Shape of Dataset with Invalid Dates Removed and Crime added: " + str(df.shape))


print("Shape of Original Dataset : " + str(df.shape))


# Create a key which is a date time object
date_time_col = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY']])
df['DateTimeMix'] = date_time_col
df.set_index('DateTimeMix', inplace=True)

df = df.sort_values(['YEAR', 'MONTH', 'DAY'], ascending=True)


# Add a new column called crimes and give it value of 1 since all dataset rows are crimes
df['Crime'] = np.ones(df.shape[0])


neighbourhood_file_path = 'cov_localareas.csv'
addresses = pd.read_csv(neighbourhood_file_path, error_bad_lines=False)
addresses = addresses['NAME']
addresses = addresses[addresses != 'Downtown']
addresses = addresses[addresses != 'Killarney']

for i in addresses:
  subset = df[df['Neighbourhood'] == i]
  df_extra = subset.groupby(level=0).count().resample('1d').asfreq()
  df_extra = df_extra[pd.isna((df_extra['DAY']))]
  df_extra['Crime'] = 0
  df_extra['YEAR'] = df_extra.index.year
  df_extra['MONTH'] = df_extra.index.month
  df_extra['DAY'] = df_extra.index.day
  df_extra['Neighbourhood'] = i
  df = df.append(df_extra)
  
df = df.sort_index()
  
print("Shape of New Dataset: " + str(df.shape))