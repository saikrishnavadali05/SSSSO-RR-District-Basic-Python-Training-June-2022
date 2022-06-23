list = [1,2,3,4,4,5,6,6,7,8]
print(list)
my_tuple = tuple(list)
print(my_tuple)
set_tuple = tuple(set(my_tuple))
print(set_tuple)

sum=0
for i in set_tuple:
    sum+=i
    print(sum)
