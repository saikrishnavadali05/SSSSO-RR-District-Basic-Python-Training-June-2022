new_tuple = input("Enter Elements of your choice seperated by a space: ").split()
mytuple = tuple(new_tuple)
print(mytuple)
alternative_tuple  = ()
for index_of_elements,elements in enumerate(mytuple):
    if index_of_elements % 2 == 0:
        alternative_tuple = alternative_tuple + (mytuple[index_of_elements],)
print("The Alternative elements of", mytuple, "are", alternative_tuple)



