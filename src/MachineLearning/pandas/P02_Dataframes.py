"""
Dataframes is a main object in Pandas.
It is used to represent data with rows and column
(tabular or excel spreadsheet like data)
"""
import pandas as pd

"""whether_Data = {
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature':[32,35,28,24,32,31],
    'windspeed':[6,7,2,7,4,2],
    'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']
}
df = pd.DataFrame(whether_Data)
# we can also make dataset using dictionary"""

df = pd.read_csv("P02.csv")
print(df)

print()

print(f"To know the dimension of table ---> {df.shape}")

print()

print("to print some value of the dataset present at the head --->")
print(df.head())  # give he convince of printing few rows

print()

print("if you want to print only two rows from the head --->")
print(df.head(2))

print()

print("To print the the dataset from the tail --->")
print(df.tail())

print()

print("if you want to print the last 2 dataset --->")
print(df.tail(2))

print()

print("let if you want to print some dataset from the middle --->")
print(df[1:4])

print()

print("To print all the column present in the dataset --->")
print(df.columns)

print()

print("To print the column at index 'n' ")
print(df.columns[2])

print()

print("To print all he data of the particular column --->")
print(df.day)  # same as df['day']

print()

print("To find the type of a particular column in dataset --->")
print(type(df.event))

print()

print(":et if you want to print 2 columns at a time --->")
print(df[['day', 'event']])

print()

print("To find the max temperature in the dataset --->")
print(df['temperature'].max())
# for standard deviation .std()

print()

print("To print the statistics of the dataset --->")
print(df.describe())

print()

# To conditionally select data from the dataframe
print(df[df.temperature >= 32])

print()

print("To get only the data with max temperature --->")
print(df[df.temperature == df.temperature.max()])
# when column name have space in between it, then use
# df[df['temperature'] == df['temperature'].max()]

print()

print("To print the day when the temperature was maximum --->")
print(df[['day', 'temperature']][df['temperature'] == df['temperature'].max()])

# list of pandas operations
# https://pandas.pydata.org/docs/reference/api/pandas.Series.html

print()
print("To get the indexing values --->")
print(df.index)

print()

print("To set the indexing of the data as day ---?")
a = df.set_index('day')  # but doesn't modify the df index as day
# to do that we can use inplace=True
# and if you want to reset the at its original, then use
# df.reset_index(inplace=True)
print(a)

print()

print("To get a particular row using index--->")
print(df.loc[1])

