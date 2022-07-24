#  Write a program to pass a list as a command line arguments. Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) 
#  Next, add all the elements of that duplicate free tuple and print the addition output.

from ssl import ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION
from sys import argv 
Numbers1 = argv[1]
Numbers2 = argv[2]
Numbers3 = argv[3]
Numbers4 = argv[4]
Numbers_Club = []
Numbers_Club = [Numbers1,Numbers2,Numbers3,Numbers4]
print("The list is", Numbers_Club) 
Numbers_Using_Set = set(Numbers_Club)
print("The Set of the list",Numbers_Club, "is",Numbers_Using_Set) 
Number_using_tuple = tuple(Numbers_Using_Set)
print("The Tuple is",Number_using_tuple)
Add1 = int(Number_using_tuple[0]) 
Add2 = int(Number_using_tuple[1])
Add3 = int(Number_using_tuple[2])
print(Add1+Add2+Add3)

