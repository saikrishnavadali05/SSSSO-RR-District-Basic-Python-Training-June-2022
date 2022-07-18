# creating variable to store the
# number of words
number_of_words = 0
 
# Opening our text file in read only
# mode using the open() function
with open('paragraph_test.txt','r') as file:
 
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
 
    # Splitting the data into separate lines
    # using the split() function
    lines = data.split()
 
    # Adding the length of the
    # lines in our number_of_words
    # variable
    number_of_words += len(lines)
 
 
# Printing total number of words
print(number_of_words)