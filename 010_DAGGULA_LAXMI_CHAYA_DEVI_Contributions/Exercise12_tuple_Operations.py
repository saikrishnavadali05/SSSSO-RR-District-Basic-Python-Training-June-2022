# Tuple operations

tup = ("pulsar", "duke", "shine")
print(tup)
# printing total no of items in tuple
Total_no_of_items = len(tup)
print("Total number of items in tuple =", Total_no_of_items)
# printing index no of item shine in tuple
index_of_shine = tup.index("shine")
print("Index of item \"shine\" in tuple:", index_of_shine)
# converting tuple to list
lst = list(tup)
# appending item to list
lst.append("Splendor")
# removing item "duke" from the list"
lst.remove("duke")
# coverting list to tuple
tup = tuple(lst)
# printing tuple
print(tup)
