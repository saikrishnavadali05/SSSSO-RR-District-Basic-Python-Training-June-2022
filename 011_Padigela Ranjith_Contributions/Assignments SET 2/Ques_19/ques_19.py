"""
19.Write a program to count the number of words in an input file that contains 
2 Huge paragraphs. (Take random text from websites containing multiple paragraphs
 and store that text in a text file). 
Perform Exception Handling for the code to work even if the input file doesn't exist.
"""

f = open("mytextpar.txt",'r')
count = 0


try:
    for line in f:
        words = line.split()
        count += len(words)
    print(count)    
except:
    print("File is not found")
f.close()