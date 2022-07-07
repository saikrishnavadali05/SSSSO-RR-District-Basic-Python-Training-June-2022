#Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys.
#Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).

dict = { 'name': 'Dinesh', 'roll_no': 11, 'Std': 11, 'course': 'Comp. Sci.'  }

print("Dictionary: ",dict)

for keys, values in dict.items():
    print(keys, ' : ', values)
    
values = dict.values()
print("values of the dictionary: ",str(values))                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                           
