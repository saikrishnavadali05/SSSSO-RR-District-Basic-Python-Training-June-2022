#7.Given a string print all the lowercase characters, upper case characters and numeric characters and their counts.
str = input("Enter any String of your choice :")
print("user entered  string :", str)
uppercase = []
lowercase = []
digits = []
specialchar = []
for i in range(len(str)):
    print(i)
    if str[i].isupper():
        print(i)
        uppercase.append(str[i])
    elif str[i].islower():
        lowercase.append(str[i])
    elif str[i].isdigit():
        digits.append(str[i])
    else:
        specialchar.append(str[i])
print("uppercase letters in the given string is  :", uppercase)
print("number of uppercase letters in a given  string is :", len(uppercase))
print("lowercase letters in the given string is :", lowercase)
print("number of lowercase letters in a given string is :", len(lowercase))
print("digits in a given string is :", digits)
print("number of digits in a given string is :", len(digits))
print("special characters in a given string is :", specialchar)
print("number of special characters in a given string is :", len(specialchar))