# Importing library to work with .csv files
import pandas as pd
import numpy as np
from os import path 

print ("------ Importing Dataset ------\n")
# final_crime contains all data
basepath = path.dirname(__file__)
finalcrimepath = path.abspath(path.join(basepath, "..","Datasets", "final_crime.csv"))

# Import file and extract specific columns
df = pd.read_csv(finalcrimepath)

# Original data shape
print("Shape of Dataset Imported: " + str(df.shape))

# Remove invalid data
df = df[pd.isnull(df['NEIGHBOURHOOD']) != pd.isnull(pd.NaT)]
print("Shape of Dataset with Invalid data removed: " + str(df.shape))

# Extract needed columns
df = df[['YEAR', 'MONTH','DAY', 'Neighbourhood', 'Latitude', 'Longitude', 'Graffiti', 'Drinking_Fountain', 'Google_Trends']] 
print("Shape of Dataset we are using: " + str(df.shape))

print("----------------------------\n")

print ("------ Adding date-time object as key ------\n")
# Create a key which is a date time object
date_time_col = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY']])

# Make the added Date the index of the dataset
df['DateTimeMix'] = date_time_col
df.set_index('DateTimeMix', inplace=True)

print(df.head(3))
print("----------------------------\n")
# Make the created key the index of the dataset
# import pandas as pd

# file_path = '../Datasets/final_crime.csv'
# neighbourhood_file_path = '../Datasets/cov_localareas.csv'

# df = pd.read_csv(file_path)

# df = df[['TYPE', 'YEAR','MONTH','DAY','HOUR','MINUTE', 'Latitude', 'Longitude', 'Neighbourhood']] 
# print("Shape of Original Dataset : " + str(df.shape))

# import numpy as np
# from random import randint
# import random

# def random_lat_lon(n):
#   '''
#     The following function will return a n length array of
#     random latitudes, longitudes and respective neighbourhood from the city of Vancouver
#   '''
#   #read the dataset
#   df = pd.read_csv(file_path)
#   df_locations = pd.read_csv(neighbourhood_file_path)

#   A = df[['Latitude','Longitude']].fillna(0)

#   A = A[ A['Latitude'] != 0 ]
#   A = A[ A['Longitude'] > -123.5 ]
#   A = A[ A['Longitude'] < -122.9 ]
#   A = A.values

#   #gnerate random indices 
#   C = np.random.randint(A.shape[0], size=(n,1))
  
#   rand_pts = A[C]
#   rand_pts = rand_pts.reshape(len(rand_pts),2)

#   #generate random offsets between -0.001 and 0.001
#   a = -0.001
#   b = 0.001

#   offset = np.random.rand(n,2)
#   offset = a + (b-a) *offset

#   final_pts = rand_pts + offset

#   data = np.empty((final_pts[:, 0].shape[0], 1), dtype='<U24')
#   location_cords = df_locations[['Latitude', 'Longitude']].values
#   addresses = df_locations['NAME'].values

#   for j, i in enumerate(final_pts):
#     data[j] = addresses[np.argmin(np.sum(np.square(i-location_cords), axis=1))]

#   final_pts = np.append(final_pts, data, axis=1)
#   return final_pts

# f = df.sort_values(['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE'], ascending=True)

# # Create a key which is a date time object
# date_time_col = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE']])

# # Add 1 for all crimes
# df['Crime'] = np.ones(df.shape[0])
# df['DateTimeMix'] = date_time_col
# df.set_index('DateTimeMix', inplace=True)

# # Remove invalid date data
# df = df[pd.isnull(df['MINUTE']) != pd.isnull(pd.NaT)]
# print("Shape of Dataset with Invalid Dates Removed: " + str(df.shape))

# df_extra = df.groupby(level=0).count().resample('30min').asfreq()
# df_extra = df_extra[pd.isna((df_extra['HOUR']))]
# df_extra['Crime'] = 0
# df_extra['TYPE'] = 'None'
# df_extra['YEAR'] = df_extra.index.year
# df_extra['MONTH'] = df_extra.index.month
# df_extra['DAY'] = df_extra.index.day
# df_extra['HOUR'] = df_extra.index.hour
# df_extra['MINUTE'] = df_extra.index.minute

# req = len(df_extra.index)
# pts = random_lat_lon(req) 

# df_extra['Latitude'] = pts[:,0]
# df_extra['Longitude'] = pts[:,1]
# df_extra['Neighbourhood'] = pts[:,2]

# print("Shape of 'No Crime' data being added: " + str(df_extra.shape))

# df = df.append(df_extra)
# df = df.sort_index()

# print("New Shape of dataset: " + str(df.shape))
# print("Sample of Dataset")
# print(df.tail(10))

# print("------------------------\n")

# # Now the dataset is complete, we can use subsets from it for multiple trainings

# # First Network: 
# #   Input  = date and time O
# #   Output = probability of crime across neighbourhoods

# X_1 = df[df['Crime'] == 1.0]

# onehot = pd.get_dummies(X_1['Neighbourhood'])
# Y_1 = onehot.as_matrix()
# target_labels = onehot.columns
# X_1 = X_1[['YEAR','MONTH','DAY', 'HOUR', 'MINUTE']]
# number_cols = X_1.shape[1]
# X_1 = X_1.values

# from keras.utils.np_utils import to_categorical
# from sklearn.model_selection import train_test_split

# #split training and validation sets randomly
# x_train_val, x_test, y_train_val, y_test = train_test_split(X_1, Y_1, train_size=0.8,test_size=0.2, random_state=101) 
# x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, train_size=0.8,test_size=0.2, random_state=101) 

# x_train = x_train.reshape(-1, 1, number_cols)
# x_val = x_val.reshape(-1, 1, number_cols)
# x_test = x_test.reshape(-1, 1, number_cols)

# print("Dataset Size: " + str(X_1.shape))
# print("Training Set Shape:" + str(x_train.shape))
# print("Validation Set Shape:" + str(x_val.shape))
# print("Test Set Shape:" + str(x_test.shape))


# # from keras import layers
# # from keras import models
# # import matplotlib.pyplot as plt

# # def plot_validation_loss(history):
# #   loss = history.history['loss']
# #   val_loss = history.history['val_loss']
# #   min_index = val_loss.index(min(val_loss))
# #   epochs = range(1, len(loss) + 1)
  
# #   plt.plot(epochs, loss, 'bo', label='Training loss')
# #   plt.plot(epochs, val_loss, 'r', label='Validation loss')
  
# #   plt.title('Training and Validation Loss')
# #   plt.ylabel('Loss')
# #   plt.xlabel('Epochs')
# #   plt.legend()
# #   plt.show()
# #   print("Minimum Val Loss: " + str(min(val_loss)) + "(" + str(min_index +1 ) + " epoches) \n\n")

  
# # model = models.Sequential()

# # model.add(layers.Dense(128, activation='relu', input_shape=(1,number_cols) ) )
# # model.add(layers.Dense(256, activation='relu') )

# # model.add(layers.Flatten())
# # model.add(layers.Dense(2, activation='softmax') )

# # model.compile(optimizer='rmsprop',
# #                 loss='categorical_crossentropy',
# #                 metrics=['accuracy'])

# # Invalid data losses

# # 54367 lost due to invalid locations


# # -------- TEST CODE --------

# # nth = 200
# # np.set_printoptions(suppress=True)
# # z = random_lat_lon(nth)
# # For printing co-ordinates with right formatting
# # for i in range(nth):
# #   print(' '.join(map(str, z[i])))

# # print("---------Target Labels---------")
# # print(target_labels)

# # print("---------One Hot---------")
# # print(Y)

# # print("---------X---------")
# # print(X)