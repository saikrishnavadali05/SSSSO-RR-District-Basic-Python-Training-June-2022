#  program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments 

from sys import argv

list = argv[1]
Reversed_list= list[::-1]
print(Reversed_list)


# from sys import argv
# 
# number_list = list()
# number_list[0] = argv[1]
# number_list[1] = argv[2]
# number_list[2] = argv[3]
# 
#  
# print(number_list)
# 
# Reversed_list = number_list.reverse()
# 
# print("Reversed List : ", Reversed_list)
# 
# #  
# import argparse
# 
# parser = argparse.ArgumentParser()
# parser.add_argument("number1", help="first number")
# parser.add_argument("number2", help="second number")
# parser.add_argument("number3", help="third number")
# args = parser.parse_args()
# 
# print(args.number1)
# print(args.number2)
# print(args.number3)
# 
# n1 = int(args.number1)
# n2 = int(args.number2)
# n3 = int(args.number3)
# 
# details = [n1, n2, n3]
# 
# print("Original list : ", details)
# 
# # Reversed_list = details.reverse() 
# # # Unable to understand why this is not getting executed
# # print("\t Reversed list : ", Reversed_list)
# 
# print("length : ", len(details))
# 
# i = details[len(details) - 1]
# 
# print("Reversed list : ")
# while i >=0:
#     print(details[i]) # what is the error? 
#     i = i-1
# 



