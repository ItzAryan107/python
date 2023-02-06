import pandas as pd
df = pd.read_csv("P01_WorkingOfPandasOnData.csv")

# printing all the values from dataset
print(df)

print()

print("To print the max temperature through out Jan in NewYork --->")
print(df["Temperature"].max())

print()

print("To know on which dates it rained --->")
print(df["Date"][df["Events"] == "Rain"])

print()

print("To get the average wind speed in the month of jan in NewYork --->")
averageWindSpeed = df["WindSpeed"].mean() # this average value is not actual, bcz in csv file
# where there is no value, means where the value is null, bcz of it giving not correct value
# means we need to change null value to zero
print(f"incorrect average value ---> {averageWindSpeed}")

print()
"""
process of cleaning messy data is called data munging or data wrangling
"""

df.fillna(0, inplace=True)  # it will change the all null value with zero
print(df)

print()

averageWindSpeed = df["WindSpeed"].mean()
print(f"correct Average value ---> {averageWindSpeed}")







