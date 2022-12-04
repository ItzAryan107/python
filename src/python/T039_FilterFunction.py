list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def isGreaterThan5(num):
    return num > 5


listGreaterThan5 = list(filter(isGreaterThan5, list1))  # this is need to be type cast into
# list or tuple else it will return the filter object

print(listGreaterThan5)



