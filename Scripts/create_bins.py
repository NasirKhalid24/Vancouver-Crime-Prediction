# Import data manipulation packages
import numpy as np
import pandas as pd
from os import path 

basepath = path.dirname(__file__)
crimepath = path.abspath(path.join(basepath, "..","Datasets", "final_crime.csv"))
neighbourhood_path = path.abspath(path.join(basepath, "..","Datasets", "cov_localareas.csv"))

final_crime = pd.read_csv(crimepath)
crime = final_crime[['YEAR','MONTH','DAY', 'Neighbourhood']] 

# Remove invalid date data
crime = crime[pd.isnull(crime['Neighbourhood']) != pd.isnull(pd.NaT)]
print("Shape of Dataset with Invalid Dates Removed and Crime added: " + str(crime.shape))

print("Shape of Original Dataset : " + str(crime.shape))


# Create a key which is a date time object
date_time_col = pd.to_datetime(crime[['YEAR',  'MONTH','DAY']])
crime['DateTimeMix'] = date_time_col
crime.set_index('DateTimeMix', inplace=True)

crime = crime.sort_values(['YEAR', 'MONTH','DAY'], ascending=True)



# Add a new column called crimes and give it value of 1 since all dataset rows are crimes
crime['Crime'] = np.ones(crime.shape[0])



addresses = pd.read_csv(neighbourhood_path, error_bad_lines=False)
addresses = addresses['NAME']


for i in addresses:
    subset = crime[crime['Neighbourhood'] == i]
    crime_extra = subset.groupby(level=0).count().resample('1d').asfreq()
    crime_extra = crime_extra[pd.isna((crime_extra['Crime']))]
  
    if(crime_extra.shape[0] != 0 ):
        crime_extra['Crime'] = 0
        crime_extra['YEAR'] = crime_extra.index.year
        crime_extra['MONTH'] = crime_extra.index.month
        crime_extra['DAY'] = crime_extra.index.day
        crime_extra['Neighbourhood'] = i
        crime = crime.append(crime_extra)

crime = crime.sort_index()
  
print("Shape of New Dataset: " + str(crime.shape))