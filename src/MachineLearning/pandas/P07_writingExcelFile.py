import pandas as pd

df = pd.read_excel("P06_readingExcelFile.xlsx")
print(df)

print()


def convert_people_cell(cell):
    if cell == "n.a.":
        return "code with rn"
    return cell


print("Let you have to write the updated data to a new excel file --->")
pd.read_excel("P06_readingExcelFile.xlsx", sheet_name="Sheet1", converters={
    'people': convert_people_cell
}).to_excel("P07_updateOfP06_01.xlsx", sheet_name="stocks01")  # here we are giving a new sheet name
df1 = pd.read_excel("P07_updateOfP06_01.xlsx", sheet_name="stocks01")

print(df1)

print()

print("Let if you don't want to write the side index number in newly formed file --->")
pd.read_excel("P06_readingExcelFile.xlsx", sheet_name="Sheet1", converters={
    'people': convert_people_cell
}).to_excel("P07_updateOfP06_withoutIndex_02.xlsx", sheet_name="stocks02", index=False)
df2 = pd.read_excel("P07_updateOfP06_withoutIndex_02.xlsx", sheet_name="stocks02")
print(df2)

print()

print("Let if you want to write the data in newly formed excel from another column and row --->")
pd.read_excel("P07_updateOfP06_withoutIndex_02.xlsx", sheet_name="stocks02").to_excel("P07_newExcel01.xlsx",
                                                                                      sheet_name="stocks03",
                                                                                      startrow=5,startcol=5)
df3 = pd.read_excel("P07_newExcel01.xlsx", sheet_name="stocks03")
print(df3)
