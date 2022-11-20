with open("T22_MoreOnFiles.txt") as file:  # here no need to close the file
    content = file.read()
    print(content)

file = open("T22_MoreOnFiles.txt")
print(file.readlines())
file.close()
