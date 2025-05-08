# Write a function that take string as a parameter. the string is given by the user as input. the final output from the function is to reverse the string.
'''
 example the string is Multiple -
  output is elpitluM
'''
mystring = input('Enter a string of your choice: ')
def reverse(x):
    return x[::-1]
print('Reverse of a string is: ', reverse(mystring))

    
