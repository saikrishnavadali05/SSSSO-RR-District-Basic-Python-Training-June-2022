"""Input : Love All Serve All Help Ever Hurt Never

Output : 
Love
All
Serve 
All 
Help
Ever
Hurt
Never"""

from posixpath import split


Input="Love All Serve All Help Ever Hurt Never"
list1=Input.split(" ")

print(list1)
##using for loop 
for i in list1:
    print(i)

## using while loop
