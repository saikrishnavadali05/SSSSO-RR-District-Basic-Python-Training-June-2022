# Write a python script that contains a dictionary with name : "details" and the script should perform the steps from 1 to 7.
# Consider the following Dictionary  :
'''
 details = {
             "name": "Steve",
             "education": "Reed College",
             "born": 1955
           }

1. Print all the keys and values from the dictionary separately.
2. Add a new key "died" and assign the value "2011" to the above dictionary. And then print the updated dictionary again.
3. Remove the "education" key from the dictionary and print the changed dictionary again.
4. Create another duplicate dictionary with name "details_duplicate" from the above dictionary to have a backup of the existing dictionary.
5. Remove all the elements of the "details" dictionary and then print the entire empty dictionary.
6. Print the entire duplicate dictionary
'''

details = {
             "name": "Steve",
             "education": "Reed College",
             "born": 1955
          }
print(details)

# 1
print('Keys are: ', details.keys())
print('values are: ', details.values())

# 2
details['died'] = '2011'
print('Updated details: ',details)

# 3
del details['education']
print('Updated details: ',details)

# 4
details_duplicate = details.copy()
print('Duplicate of details: ', details_duplicate)

# 5
details.clear()
print(details)

# 6
print('Duplicate of details: ', details_duplicate)