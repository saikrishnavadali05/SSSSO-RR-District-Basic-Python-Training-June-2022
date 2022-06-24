# program to pass a list as a command line arguments. Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.

from sys import argv

list_O = argv[1]  # note: enter the list elements without [], simply enter elements with ,
conversion_TL = tuple(list_O.split(","))
res = tuple(set(conversion_TL))

print("Tuple without duplicate elements : ", res)

result = tuple(int(num) for num in res.replace('(', '').replace(')', '').replace('...', '').split(', '))

print(result)


# new_tuple = ()
# 
# for i in res:
#     for sub_i in i.split(","):
#         new_tuple.append(int(sub_i))
# 
#     