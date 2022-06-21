# Input the elements into a list
group_of_elements = input("Enter the Integer Elements of your choice 'seperated by a space': ").split()
print(group_of_elements)

# remove duplicates from the list
elements_without_duplicates = set(group_of_elements)
print(elements_without_duplicates)

# set to tuple
mytuple = tuple(elements_without_duplicates)
print(mytuple)

# sum of tuple elements
sum = 0
for elements in mytuple:
    sum = sum + int(elements)
print(sum)


