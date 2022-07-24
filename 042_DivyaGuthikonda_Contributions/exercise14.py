details = {
             "name": "Steve",
             "education": "Reed College",
             "born": 1955
           }

#1        
for key,value in details.items():
    print(key,value)
# name Steve
# education Reed College
# born 1955

#2
details["died"]=2011
print(details)
#{'name': 'Steve', 'education': 'Reed College', 'born': 1955, 'died': 2011} 

#3
del details["education"]
print(details)
#{'name': 'Steve', 'born': 1955, 'died': 2011}

#or
print(details.pop("education"))
print(details)
#{'name': 'Steve', 'born': 1955, 'died': 2011}

#4
duplicate_dict_of_details=details.copy()
print(duplicate_dict_of_details)
#{'name': 'Steve', 'education': 'Reed College', 'born': 1955}

#5
print(details.clear())
#None

#6
print(duplicate_dict_of_details)