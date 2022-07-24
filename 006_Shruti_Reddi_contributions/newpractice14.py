import pickle

def createFile():
    file = open("book.dat","ab")
    BookNo = int(input("Enter book number: "))
    Book_Name = input("Enter book Name: ")
    Author =input("Enter author: ")
    Price = int(input("Enter price: "))
    record = [BookNo, Book_Name, Author, Price]
    pickle.dump(record, file)
    file.close()
    
def countRec(Author):
    file = open("book.dat","rb")
    count = 0
    try:
        while True:
            record = pickle.load(file)
            if record[2]==Author:
                count+=1
    except EOFError:
        pass
    return count
    file.close()

#To test working of functions
def testProgram():
    while True:
        createFile()
        choice = input("Add more record (y/n)? ")
        if choice in 'Nn':
            break
    Author = input('Enter author name to search: ')
    n = countRec(Author)
    print("No of books are",n)

testProgram()    
    