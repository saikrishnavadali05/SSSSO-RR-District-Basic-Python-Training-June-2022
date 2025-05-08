# input string from user
str = input("Enter any String:")
print("original string:", str)
# initialising uppercaselist
uppercase = []
# initializing lower case list
lowercase = []
# initializing digits list
digits = []
# initializing special characters
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

# displaying uppercase chaaracters
print("uppercase letters:", uppercase)
print("number of uppercase letters:", len(uppercase))
# displaying lowercase chaaracters
print("lowercase letters:", lowercase)
print("number of lowercase letters:", len(lowercase))
# displaying digits
print("digits:", digits)
print("number of digits:", len(digits))
# displaying specialchaaracters
print("special letters:", specialchar)
print("number of special letters:", len(specialchar))
