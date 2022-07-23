"""
13.Write a function that accepts a sentence from a paragraph stored in a 
text file input.txt 
and calculates the number of letters and digits within that sentence string.
"""

import re
def acceptSentence():
    f = open("my_text.txt","r")
    digit_count = 0 
    letter_count = 0
    for i in f.readlines():
        no_of_str = i.rstrip().split()
        for j in range(0,len(no_of_str)):
            words = re.split("a-zA-Z\W",no_of_str[j])
            for word in words:
                if word.isdigit():
                    digit_count += len(word)
                else:
                    letter_count += len(word)
    f.close()
    return "The number of digits is",digit_count ,"The number of letters is", letter_count

print(acceptSentence())