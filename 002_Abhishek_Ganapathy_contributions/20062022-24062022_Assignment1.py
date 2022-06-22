# Write a program to print each word of the line in a new line using both while and for loops.

String1 = (input("Enter the String "))
print("The String is",String1)
Splitted_String = list(String1.split())
print("The String is split as", Splitted_String)
for i in Splitted_String:
    print(i)

