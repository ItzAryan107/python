file = open("T21_FileWriting.txt", "w")
file.write("Aryan Bhai Bhut Ache Ha!!\n")

"""
here it will create the file and write all the content, what you want
and if the file already exist then it will erase all the content of the file and write the new content
in that file
"""
file.close()

# now let if we want to add or append the content to the file than, instead of giving parameter
# "w" we need to give "a"

file1 = open("T21_FileWriting.txt", "a")
a = file1.write("Aryan is a good boy\n")  # it returns the number of character writen
print(a)
file1.close()
