#Write a python script that does the following operations:
#Input to the script will be a tuple with bike names : ("pulsar", "duke", "shine")

#1. give the total number of items present in the tuple.
#2. give the index number for "shine" in the tuple.
#3. add the item "splendor" to the tuple.
#4. remove the item "duke" from the tuple.

tuple1 =("pulsar", "duke", "shine")
print(len(tuple1))

print("The number of shine in tuple is :", tuple1.index("shine"))
tuple1 =tuple1 + ("splendor",)
print(tuple1)
list1=list(tuple1)
del list1[1]
b=tuple(list1)
print(b)