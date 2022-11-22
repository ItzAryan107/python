file = open("T21_FileWriting.txt", "a")  # here "a" mode allows you to append the
# content
file.write("Anup is the friend of Aryan\n")
file.write("Karthika is the friend of Anup\n")
file.close()


file1 = open("T21_FileWriting.txt", "r+")  # to read and write both
content = file1.read()
print(content)
file1.write("Thank you")
print(content)
file1.close()
