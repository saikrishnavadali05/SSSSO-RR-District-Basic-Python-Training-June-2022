# Write a python script that contains a dictionary with name : "details" and the script should perform the steps from 1 to 7.

details = {
             "name": "Steve",
             "education": "Reed College",
             "born": 1955
           }

# 1. Print all the keys and values from the dictionary separately.
print("---------")
print("The Keys are:")
for keys in details.keys():
    print(keys)
print("---------")
print("The values are:")
for values in details.values():
    print(values)
# Add a new key "died" and assign the value "2011" to the above dictionary. And then print the updated dictionary again.
print("---------")
details["died"] = 2011
print(details)
# Remove the "education" key from the dictionary and print the changed dictionary again.
print("---------")
details.pop("education")
print(details)
# Create another duplicate dictionary with name "details_duplicate" from the above dictionary to have a backup of the existing dictionary.
print("---------")
detail_duplicate = details.copy()
print("duplicate",detail_duplicate)
print("Original",details)
# Remove all the elements of the "details" dictionary and then print the entire empty dictionary.
print("---------")
details.clear()
print(details)
# Print the entire duplicate dictionary
print(detail_duplicate)