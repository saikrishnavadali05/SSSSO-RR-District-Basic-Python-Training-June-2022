# Given a string print all the lowercase characters, upper case characters and numeric characters and their counts.

# Reading input string
input_string = input("Enter a string: ")
char_count = {}


upper_case_char = set([i for i in input_string if i.isupper()])
lower_case_char = set([i for i in input_string if i.islower()])
digits = set([i for i in input_string if i.isdigit()])

for i in input_string:
    char_count[i] = char_count.get(i, 0) + 1

print("The upper case character in the given string are: ")
for i in upper_case_char:
    print(i, end = " ")
print()

print("The lower case character in the given string are: ")
for i in lower_case_char:
    print(i, end = " ")
print()

print("The digits in the given string are: ")
for i in digits:
    print(i, end = " ")
print()

print("The count of the characters in the give string are: ")
for k, v in char_count.items():
    print(k,":",v)
