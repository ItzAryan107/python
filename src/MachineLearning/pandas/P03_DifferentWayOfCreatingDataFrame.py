import pandas as pd
# 1. To directly reading the csv file
df = pd.read_csv("P02.csv")
print(df)

print()

# 2. creating a dataframe using excel file
# this is getting possible in jupyter notebook, have a look there

print()

# 3. creating dataframe using python dictionary
whether_Data = {
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature':[32,35,28,24,32,31],
    'windspeed':[6,7,2,7,4,2],
    'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']
}
df = pd.DataFrame(whether_Data)
print(df)

print()

# 4. creating dataframe using list of tuples
weather_Data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(weather_Data, columns=['day', 'temperature','windspeed','event'])
print(df)

print()

# 5. creating dataframe using list of dictionary
weather_Data = [
    {'day':'1/1/2017','temperature':32,'windspeed':6,'event':'Rain'},
    {'day':'1/2/2017','temperature':35,'windspeed':7,'event':'Sunny'},
    {'day':'1/3/2017','temperature':28,'windspeed':2,'event':'Snow'}
]
df = pd.DataFrame(weather_Data)
print(df)


# https://pandas.pydata.org/docs/user_guide/io.html
