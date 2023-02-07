import pandas as pd

df = pd.read_excel("P06_readingExcelFile.xlsx", "Sheet1")
print(df)

print()

i = 0
def convert_people_cell(cell):
    global i
    if cell == "n.a.":
        print(pd.read_excel("P06_readingExcelFile.xlsx", "Sheet1").loc[i])
        name = input("Enter People for the given dataset ---> ")
        i = + 1
        return name
    i = + 1
    return cell

df1 = pd.read_excel("P06_readingExcelFile.xlsx", "Sheet1", converters={
    'people' : convert_people_cell
})
print(df1)  # here the data will not change in the excel file, it will only get change in the df1 variable
#  bcz we reading the file here, not writing the file






