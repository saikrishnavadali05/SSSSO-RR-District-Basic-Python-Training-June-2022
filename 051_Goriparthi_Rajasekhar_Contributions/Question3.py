#Question3 : Write a program to print all the elements within a list
#  in the reverse order. The entire list has to be passed via command 
# line arguments (Hint : use argv)

import sys
  
  
print("This is the name of the program:",
       sys.argv[0])

Alphabets = list(sys.argv)
Alphabets.reverse()
print("print reverse list = ",Alphabets)