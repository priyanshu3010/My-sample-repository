import pandas as pd

r=pd.read_csv('trainwax.csv')
print(r.head())
print(r.shape)
print(r.describe())