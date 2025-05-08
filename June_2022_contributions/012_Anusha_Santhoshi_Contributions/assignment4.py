#Write a program to print all the alternative elements of a tuple.
#The elements to the tuple have to be given to the program using input() function.

tuple_list=input("Enter elements seperated by ,to tuple")
given_list1=tuple_list.split(',')
alt_listtuple=tuple(given_list1)
for i in range(0,len(alt_listtuple),2):
    print("alternate elements of a tuple",alt_listtuple[i])

# PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> python assignment4.py
# Enter elements seperated by ,to tuple Sai ,Ram ,Krishna ,RangaReddy
# alternate elements of a tuple  Sai 
# alternate elements of a tuple Krishna 
# PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> 
