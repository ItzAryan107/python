import pandas as pd
df = pd.read_csv("P04_StockData.csv")
print(df)

print()

print("If you want that the interpreter do not read the first line --->")
print(pd.read_csv("P04_StockData.csv", skiprows=1))
# this will skip 1 row from the top

print()

print("If you want to rea csv from the first row, leaving row at index 0 --->")
print(pd.read_csv("P04_StockData.csv", header=1))
# here header works on index, so here it will make the table row at 1st index as header

print()

print("Let here in the csv file no header is given --->")
print(pd.read_csv("P04_StockData.csv", header=None))
# giving header=None it will automatically generate the numbers n the header, which can be named even

print()

print("Let there is no header and you want to give the header --->")
print(pd.read_csv("P04_StockData.csv", header=None, names=["A", "B","C","D","E"]))
# now the header gonna name as A B C D...

print()

print("Lt if you want to read some rows from your dataframe --->")
print(pd.read_csv("P04_StockData.csv", nrows=3))
# it will read from index 0 to index 2

print()

print("let if you want to read those rows whose any column wont have there data and replace it with NaN -->")
print(pd.read_csv("P04_StockData.csv", na_values=["not available", "n.a."]))

print()

print("Let ypu have a column which can not be negative, and by chance a negative value is there in that column, "
      "and you want to convert that to NaN --->")
# which can be done by using dictionary
print(pd.read_csv("P04_StockData.csv", na_values={
    'eps':["not available", "n.a."],
    'revenue':["not available", "n.a.",-1],
    'price':["not available", "n.a."],
    'people':["not available", "n.a."]
}))


