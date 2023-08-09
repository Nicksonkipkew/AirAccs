import pandas as pd
from datetime import datetime

#Load the dataset into a Pandas DataFrame:
df = pd.read_csv('airAccs.csv')

#Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
#Convert the 'Aboard' column to integer format
df['Aboard'] = df['Aboard'].astype('Int64')
#Create the 'accident_delta' column to calculate the time difference from January 1, 1997
reference_date = datetime(1997, 1, 1)
df['accident_delta'] = df['Date'].apply(lambda x: (x - reference_date).days)
#Determine the number of exact duplicates in the dataset
exact_duplicates = df.duplicated()
num_exact_duplicates = sum(exact_duplicates)
print("Number of exact duplicates:", num_exact_duplicates)

#Remove duplicates from the dataset based on the attribute subset ['Date', 'operator', 'Aboard']
df.drop_duplicates(subset=['Date', 'operator', 'Aboard'], inplace=True)
#Identify probable duplicates by examining the data for common patterns or similarities. One approach
#could be to check for rows with similar values in multiple columns, such as 'Date',
#'operator', 'planeType', and 'Aboard'. For example
probable_duplicates = df[df.duplicated(subset=['Date', 'operator', 'planeType', 'Aboard'], keep=False)]
#To filter out probable duplicates, you can investigate the probable duplicate
#rows further by examining additional columns or conducting manual inspection.
#Look for similarities or patterns that indicate duplicate entries,
#such as matching descriptions, locations, or other relevant attributes.
#Based on your findings, you can decide to remove or merge the probable duplicates.

print(df)
