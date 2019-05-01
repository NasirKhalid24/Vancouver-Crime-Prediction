# Import data manipulation packages
import numpy as np
import pandas as pd
from os import path 

basepath = path.dirname(__file__)
trendpath = path.abspath(path.join(basepath, "..","Datasets", "googletrend.csv"))
crimepath = path.abspath(path.join(basepath, "..","Datasets", "final_crime.csv"))


# Importing the data
googletrend = pd.read_csv(trendpath, index_col='Month')
#googletrend = pd.read_csv('googletrend.csv')

# Importing CSV file and extracting required portion
final_crime = pd.read_csv(crimepath)
final_crime = final_crime[final_crime['YEAR'] > 2003]

#creating a numpy array of dataset
crimes = final_crime
crimes = np.array(crimes)

#creating a numpy array of google trends
googletrend = np.array(googletrend)
trendvalue = []

for crime in crimes:
    #obtain the year and month of each crime
    y = crime[1]
    m = crime[2]

    #map it to the previous month in the other dataset 
    offset = (y - 2004)*12 + m - 1 - 1
    #print('Year: '+ str(y) + '  Month: ' + str(m) + '   Trend:' + str(googletrend[offset]))
    
    #store google trend value of the word 'crime' in an array
    trendvalue.append(googletrend[offset][0])

final_crime['Google Trends'] = trendvalue
print(final_crime)