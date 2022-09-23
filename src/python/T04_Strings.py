myStr = "Aryan is a good boy"
print(myStr)  # in string indexing starts from '0', and from end indexing start with -1

print()

print(myStr[:5])

print()

print("To get a particular character in  a string --->", myStr[5])  # if the index get >= length of the particular
# string, it will give error

print()

print("""This will give error ---> myStr[78]
but
myStr[0:78] wont --->""", myStr[:78])

print()

print("To print the length of string --->", len(myStr))

print()

print("Printing every element at interval of 2 --->", myStr[::2])

print()

print("To make the string opposite --->", myStr[::-1])
print("To make the string opposite and print the character at interval of 2 --->", myStr[::-2])

print()

print("To know whether the string contain space or not(means if there is no space its alphaNumeric) --->",
      myStr.isalnum())

print()

var1 = "aryan"
print("To know whether the string only contain alpha or not --->", var1.isalpha())
# there can only be alpha or character, there should be no space, number or any special character

print()

print("To know a particular string end with a give particular string or not --->", var1.endswith("n"))

print()

print("To count a particular character or string in a given string --->", myStr.count("a"))

print()

print("To capitalize the first letter of a given string --->", var1.capitalize())

print()

print("to find the starting index of particular string or character in a given string --->", myStr.find("is"))

print()

print("To Lower the every character of a string in lowerCase --->", myStr.lower())

print()

print("To Upper the every character of a string in upperCase --->", myStr.upper())

print()

print("To replace any character or String with another character or string in a given String --->", myStr.replace("is",
                                                                                                                  "is a"
                                                                                                                  ))

# for String functions ---> https://www.geeksforgeeks.org/python-string-methods/
