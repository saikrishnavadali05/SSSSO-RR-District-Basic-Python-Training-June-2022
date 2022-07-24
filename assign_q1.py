# Write a program to print each word of the line in a new line using both while and for loops.

sentence1= (input("Enter the String "))
print("The String is",sentence1)
Splitted_sentence= list(sentence1.split())
print("The String is split as", Splitted_sentence)
for i in Splitted_sentence:
    print(i)