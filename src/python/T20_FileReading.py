file = open("T20_FileReading.txt")  # here f is a file pointer, ,means open() function
# return file pointer

content = file.read()
print(content)

# it is very important to know, if you have open the file its need to be closed too
file.close()

print()

file2 = open("T20_FileReading.txt", "r")
# in the above line 'r' indicates to reade the file, which can be used with the open function
content = file2.read()
print(content)

file2.close()

print()

file3 = open("T20_FileReading.txt", "rb")
# here 'rb' means, the interpreter will read the file in binary form
content = file3.read()
print(content)

file3.close()

print()

file4 = open("T20_FileReading.txt", "rt")
# here 'rt' means, the interpreter will read the file in text form
content = file4.read(5)  # here it will read 5 characters only
print(content)

content = file4.read(5)  # now it will read 5 characters, the characters just after the all
# already read characters
print(content)

file4.close()

print()

file5 = open("T20_FileReading.txt", "rt")  # rt is the default mode
content = file5.read(7565)  # as 7565 characters are not there in the text file, but still it
# will read all the present characters(maybe be less than 7565)

print(content)
# if ypu are printing again the content, the content will be empty
file5.close()


print()


file6 = open("T20_FileReading.txt", "rt")
# how to read character by character content
content = file6.read()  # if any parameter given to the read function, then the pointer
# will only read that number of characters

for line in content:
    print(line)

file6.close()

print()

file7 = open("T20_FileReading.txt", "rt")
# how to read line by line content
for line in file7:
    print(line)

# the above for loop, before every line change it reads \n, that's it print a
# space line after printing a line from the content

file7.seek(0)  # this line takes the file pointer back to the character position, what u gave in the parameter
# let there should be a no space line, just after printing a line from the content
print()
for line in file7:
    print(line, end="")
file7.close()


print()
print()

file8 = open("T20_FileReading.txt")
""" In text file, i any line get end, then it end with new line character, so if the pointer is taking just one line
then it will too take new line character, and together printing a line content it will also print the space line"""

# to read just a line, we use readLine() function
print(file8.readline(), end="")


# if you try to use readline function once again, then it will read the next line, bcz pointer moved forward now
print(file8.readline(), end="")

# if the readline contain a parameter then it will read that number of characters of that particular line
print(file8.readline(5))

# and again if you using the readline function then it will read all the left characters of that line
print(file8.readline())
file8.close()


print()


file9 = open("T20_FileReading.txt", "r")
# to put every line in list ---> use readlines() function
print(file9.readlines())
file9.close()





