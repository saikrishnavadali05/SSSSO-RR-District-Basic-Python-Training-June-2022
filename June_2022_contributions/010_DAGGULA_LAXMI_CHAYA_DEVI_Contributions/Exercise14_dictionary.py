# input dictionary
details = {
    "name": "Steve",
    "education": "Reed College",
    "born": 1955
}
# printing all keys in details
for key in details.keys():
    print(key, end=" ")
print()
# printing valuesin details
for value in details.values():
    print(value, end=" ")
print()
# adding new key died and 2011 as its value
details["died"] = 2011
print(details)
# removing education from dictionary and printing updated dictionary
details.pop("education")
print(details)
# creating duplicate dictionary details_duplicate
details_duplicate = details.copy()
# removing all elements from details dictionary
details.clear()
print("After deleting all elements details:", details)
# printing duplicate dictionary
print("duplicate details:", details_duplicate)
