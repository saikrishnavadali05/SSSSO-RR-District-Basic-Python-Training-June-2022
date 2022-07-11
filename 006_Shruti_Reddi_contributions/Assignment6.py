#Given a string print all the lowercase characters, 
# upper case characters and 
# numeric characters and their counts.

string_name=input("Enter a string : ")

upper = ''
for char in string_name:
    #check uppercase characters
    if char.isupper():
        upper += char

# print uppercase characters
print('Uppercase characters:', upper, len(upper))

lower = ''
for char in string_name:
    #check lowercase characters
    if char.islower():
        lower += char

# print lowercase characters
print('Lowercase characters:', lower,len(lower))

number = ''
for num in string_name:
    #check numeric characters
    if num.isdigit():
        number += num

# print numeric characters
print('Numeric characters:', number, len(number))
