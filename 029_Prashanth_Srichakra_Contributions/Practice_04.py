# Write a program to print ASCII value of a character and vice versa.

# Char to ASCII
char = input("Enter a character: ")
ascii = ord(char)
print(f'ASCII value of {char} is {ascii}.')

# ASCII to Char
ascii = int(input("Enter ASCII value: "))
char = chr(ascii)
print(f"Character having ASCII value {ascii} is {char}.")