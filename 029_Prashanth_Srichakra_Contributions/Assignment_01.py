# Write a program to print each word of the line in a new line using both while and for loops.
s = input("Enter a string: ")
split = s.split(" ")

print("Printing splitted words using for loop")
for i in split:
    print(i)

print("Printing splitted words using while loop")
i = 0
while i<len(split):
    print(split[i])
    i += 1

print(split)