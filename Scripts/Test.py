import pandas as pd
import numpy as np

file_path = '../Datasets/cov_localareas.csv'
file_path2 = '../Datasets/final_crime.csv'

df_localareas = pd.read_csv(file_path)
df_crimes = pd.read_csv(file_path2)

x = df_crimes['NEIGHBOURHOOD']
y = df_crimes['Neighbourhood']

z = x + y
print(z)