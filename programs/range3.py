"""

Write a program to accept a string from the user and display characters that are present at an even index number.
For example, str = "pynative" so you should display 'p', 'n', 't', 'v'.

"""
# accept input string from a user
word = input('Enter word ')
print("given String:", word)

#fill the code


#solution

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])