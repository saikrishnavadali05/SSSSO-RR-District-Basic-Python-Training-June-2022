'''
Write a python script that does the following operations:
Input to the script will be a tuple with bike names : ("pulsar", "duke", "shine")

*Script should* : 
1. give the total number of items present in the tuple.
2. give the index number for "shine" in the tuple.
3. add the item "splendor" to the tuple.
4. remove the item "duke" from the tuple.
'''

bikes=("pulsar", "duke", "shine")
print("Total Number of items present in a tuple are ",len(bikes))
# Total Number of items present in a tuple are  3

print("index of shine ", bikes.index("shine"))
# index of shine  2

bikes1=list(bikes)
bikes1.append("splender")
bikes2=tuple(bikes1)
print("after modifying ",bikes2)
# after modifying  ('pulsar', 'duke', 'shine', 'splender')

bikes3=list(bikes2)
bikes3.remove("duke")
bikes4=tuple(bikes3)
print("the tuple after removing duke ",bikes4)
# the tuple after removing duke  ('pulsar', 'shine', 'splender')
