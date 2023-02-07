import pandas as pd

df = pd.read_csv("P04_StockData.csv", na_values={
    'eps': ["not available", "n.a."],
    'revenue': ["not available", "n.a.", -1],
    'price': ["not available", "n.a."],
    'people': ["not available", "n.a."]
})
print(df)

print()

print("Writing all the above data into a new csv file --->")
df.to_csv("P05_updated.csv")
df1 = pd.read_csv("P05_updated.csv")  # by default it will write the index also to the csv file
print(df1)

print()

print("Let if you don't want to write the index in your updated csv file -->")
df.to_csv("P05_updatedWithoutIndex.csv", index=False)
df2 = pd.read_csv("P05_updatedWithoutIndex.csv")
print(df2)

print()

print("Let if you want to make the new csv file which contains onl some of the columns --->")
print(df.columns)
df.to_csv("P05_updatedWithoutIndex.csv", columns=['tickers', 'revenue', 'price'], index=False)
df3 = pd.read_csv("P05_updatedWithoutIndex.csv")
# we can change the any particular csv file as many times
print(df3)

"""
Let if you want not to add header to the new csv file
then use 
* header=False
"""

