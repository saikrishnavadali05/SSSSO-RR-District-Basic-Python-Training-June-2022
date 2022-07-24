#Exercise - 14
#Write a python script that contains a dictionary with name : "details" and the script should perform the steps from 1 to 7.
#Consider the following Dictionary  :

from turtle import clear


dict_1 = {"name": "Steve", "education": "Reed College", "born": 1955}

#1. Print all the keys and values from the dictionary separately.
print(dict_1.keys())
print(dict_1.values())
#2. Add a new key "died" and assign the value "2011" to the above dictionary. And then print the updated dictionary again.
dict_1["dies"] = 2011
print(dict_1)
#3. Remove the "education" key from the dictionary and print the changed dictionary again.
dict_1.pop("education")
print(dict_1)
#4. Create another duplicate dictionary with name "details_duplicate" from the above dictionary to have a backup of the existing dictionary.
dict_duplicate=dict_1.copy()
print(dict_duplicate)
#5. Remove all the elements of the "details" dictionary and then print the entire empty dictionary.
dict_1.clear()
print(dict_1)
#6. Print the entire duplicate dictionary
dict_duplicate.clear()
print(dict_duplicate)