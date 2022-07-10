#Lower case characters,Uppercase characters,digits and their counts in a given string

test_str = "PYTHON program 7 out of 20 in set2"
print("The original string is : "+ str(test_str))
res1 = [char for char in test_str if char.islower()]
print("The lower case characters in the string are : " + str(res1))
print(len(res1))
res2 = [char for char in test_str if char.isupper()]
print("The upper case characters in the string are : " + str(res2))
print(len(res2))
res3 = [char for char in test_str if char.isdigit()]
print("The digits in the string are : " + str(res3))
print(len(res3))