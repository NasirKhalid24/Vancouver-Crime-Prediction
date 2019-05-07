# Import data manipulation packages
import numpy as np
import pandas as pd
from os import path 
import matplotlib.pyplot as plt

basepath = path.dirname(__file__)
crimepath = path.abspath(path.join(basepath, "..","Datasets", "final_crime.csv"))
neighbourhood_path = path.abspath(path.join(basepath, "..","Datasets", "cov_localareas.csv"))
binspath = path.abspath(path.join(basepath, "..","Datasets", "crime_ymd_bins.csv"))

final_crime = pd.read_csv(crimepath)
crime = final_crime[['YEAR','MONTH','DAY', 'Neighbourhood']] 


print("Shape of Original Dataset : " + str(crime.shape))

# Create a key which is a date time object
date_time_col = pd.to_datetime(crime[['YEAR',  'MONTH','DAY']])
crime['DateTimeMix'] = date_time_col
crime.set_index('DateTimeMix', inplace=True)

crime = crime.sort_values(['YEAR', 'MONTH','DAY'], ascending=True)



# Add a clustered_crime column called crimes and give it value of 1 since all dataset rows are crimes
crime['Crime'] = np.ones(crime.shape[0])

addresses = pd.read_csv(neighbourhood_path, error_bad_lines=False)
addresses = addresses['NAME']

final_dataset = pd.DataFrame()
for i in addresses:
    subset = crime[crime['Neighbourhood'] == i]

    crime_extra = subset.groupby(level=0).count().resample('1d').asfreq()

    no_crime = crime_extra[pd.isna((crime_extra['Crime']))]
    
    if(no_crime.shape[0] != 0 ):
        no_crime['Crime'] = 0
        no_crime['YEAR'] = no_crime.index.year
        no_crime['MONTH'] = no_crime.index.month
        no_crime['DAY'] = no_crime.index.day
        no_crime['Neighbourhood'] = i

        subset = subset.append(no_crime)

    clustered_subset = subset.resample('1d').sum()
    clustered_subset['YEAR'] = clustered_subset.index.year
    clustered_subset['MONTH'] = clustered_subset.index.month
    clustered_subset['DAY'] = clustered_subset.index.day
    clustered_subset['Neighbourhood'] = i
    

    final_dataset = final_dataset.append(clustered_subset)


print("Shape of final_dataset Dataset: " + str(final_dataset.shape))

crimes = np.array(final_dataset)

bins =[]
for c in crimes:
  
  count = c[3]
  if count < 2:
    case = 0
  
  elif count < 4:
    case = 1
    
  elif count < 6:
    case = 2
    
  else:
    case = 3
    
  bins.append(case)


final_dataset['Bins'] = bins
print(final_dataset)

final_dataset.to_csv(binspath, index=False)
