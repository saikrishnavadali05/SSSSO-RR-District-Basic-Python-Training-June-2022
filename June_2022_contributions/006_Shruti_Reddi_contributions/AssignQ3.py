#Write a program to print all the elements within a list in the reverse order. 
#The entire list has to be passed via command line arguments (Hint : use argv)

#sample list 
#my_list= PYTHONTRAINING

from sys import argv
my_list=argv[1]
print(my_list[::-1])