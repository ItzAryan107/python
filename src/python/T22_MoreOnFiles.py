file = open("T22_MoreOnFiles.txt")
print(file.tell())  # it tell where the pointer is, means that position s ready to write
print(file.readline())
print(file.tell())
print(file.readline())
print(file.tell())

# to reset the file pointer to the starting point
file.seek(0)
print(file.tell())
print(file.readline())

file.close()
