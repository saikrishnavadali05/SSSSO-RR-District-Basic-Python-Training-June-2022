#19.Write a program to count the number of words in an input file that contains 2 Huge paragraphs. (Take random text from websites containing multiple paragraphs and store that text in a text file). Perform Exception Handling for the code to work even if the input file doesn't exist.
number_of_words = 0 
with open(r"C:\Users\UDAY\Desktop\india.txt",'r') as file: 
    data = file.read()
    lines = data.split()
    number_of_words += len(lines)
print(number_of_words)