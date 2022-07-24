#Given a string print all the lowercase characters, upper case characters and n
# umeric characters and their counts.

input_string = input("Enter the string without any special chrecter")
upper_lst = []
lower_lst = []
number_lst = []
def Count(input_string):
    upper, lower, number,  = 0, 0, 0
    for i in range(len(input_string)):
        if input_string[i].isupper():
            upper_lst.append(input_string[i])
            upper += 1
       
        elif input_string[i].islower():
            lower_lst.append(input_string[i])
            lower += 1
    
        elif input_string[i].isdigit():
            number_lst.append(input_string[i])
            number += 1
       
        
        
    print('Upper case letters:', upper_lst)
    print('Lower case letters:', lower_lst)
    print('Number:', number_lst)
    print('\n count of Upper case letters is:', upper)
    print('count of Lower case letters is:', lower)
    print('count of numbers is:', number)
    
 

Count(input_string)