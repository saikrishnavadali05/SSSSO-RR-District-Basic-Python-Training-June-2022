# To print each word of the line in a new line using both while and for loops

input = "Love All Serve All Help Ever Hurt Never"

# for loop
words = input.split() # split function splits the sentence word by word but fails in case when string has punctuation marks (in that case re.findall() can be used) 

for i in words:
     print(i)

print("\t")
# While loop

while ' ' in input:
    i = input.index(' ')
    print(input[:i])
    input = input[i+1:]
print(input)


