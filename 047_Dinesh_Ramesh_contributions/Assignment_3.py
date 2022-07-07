#Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments (Hint : use argv)


from sys import argv

list1=list(argv[1])
print("The original list is:",list1)
print("\nThe reversed is list is:",list1[::-1])
