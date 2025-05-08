#13.Write a function that accepts a sentence from a paragraph stored in a text file input.txt and calculates the number of letters and digits within that sentence string.
f = open(r"C:\Users\SRIKANTH\Desktop\input_name.txt","r")
text = f.read()
digit=letter=0
for char in text:
    if char.isdigit():
        digit=digit+1
    elif char.isalpha():
        letter=letter+1
    else:
        pass
print("Letters:",letter)
print("Digits:",digit)