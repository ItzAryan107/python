def allBooksInTheLibrary():
    with open("T22_Books.txt", "r") as file:
        allBooks = file.readlines()

    return allBooks


def addBookInTheLibrary(bookName):
    bookName = bookName + "\n"

    """
    this code is for when u want ot write a line only one time
    allBooks = allBooksInTheLibrary()
    if not allBooks.__contains__(bookName):
        with open("T22_Books.txt", "a") as file:
            file.write(bookName)
    """

    with open("T22_Books.txt", "a") as file:
        file.write(bookName)
    print(allBooksInTheLibrary())


a = input("Enter Book Name ---> ")
addBookInTheLibrary(a)

count = 0
for book in allBooksInTheLibrary():
    if book == "Biology\n":
        count += 1

print(count)
