#Write a program to pass a list as a command line arguments. Next, convert that list into a tuple after/n
#  removing all the duplicate elements. (hint : use set) Next, add all the elements of that duplicate free tuple /n
# and print the addition output.

given_list=[1,2,3,4,5,6,8,5,2,1,4,63,2,5,7,22,1,2,3]
print(given_list)
print("the final tuple after removing all the duplicate elements from the given list by using set function: ",tuple(set(given_list)))

print("The length of the set: ",len(set(given_list)))
print("Addition of the duplicate free tuple: ",sum(tuple(given_list)))
#adding the elements of the tuple by using sum function
#output
'''
[1, 2, 3, 4, 5, 6, 8, 5, 2, 1, 4, 63, 2, 5, 7, 22, 1, 2, 3]
the final tuple after removing all the duplicate elements from the given list by using set function:  (1, 2, 3, 4, 5, 6, 7, 8, 22, 63)
The length of the set:  10
Addition of the duplicate free tuple:  146
'''