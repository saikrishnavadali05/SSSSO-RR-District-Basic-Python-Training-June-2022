#7.	Write a program to print this pattern (hint : use \t and \n wherever required).
#           *
#      * python *
#    * is  *  a    *
#* good  * programming * language *
#* to * learn * for * beginners *

#uisng Escape sequences print output
#'\n' - Newline character
#'\r' - Return character
#'\b' - Backspace character
#'\' - Backslash character
#'\”' - Double quote character
#'\’' - Single quote character
#'\t' - Tab character
#'\a' - Alarm character

list =print(list("python is a good programming to learn for beginners"))
#output=['p', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'o', 'o', 
# 'd', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 't', 'o', ' ', 'l',
#  'e', 'a', 'r', 'n', ' ', 'f', 'o', 'r', ' ', 'b', 'e', 'g',
#  'i', 'n', 'n', 'e',
#'r', 's']

#define string
string="python is a good programming to learn for beginners"
#print the given string
print("python is a good programming to learn for beginners")

#print the string in the given pattern given in quetion by using Escape sequences
#this is required ouyput
#           *
#      * python *
#    * is  *  a    *
#* good  * programming * language *
#* to * learn * for * beginners *

print("\t\t\t\t*\n\t\t\t * python * \n\t\t\t* is *\t a \t *\n\t\t*good * programming * language *\n\t* to * learn *for *beginners*")

#output as alphabet pattern
#A A A A A
#B B B B
#C C C
#D D
#E
# patterns of alphabets
i = 0
j = 0
n = 5
for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print(chr(ord('A') - 1 + i), end=" ")
    print("")

#output of number pattern
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1
    depth = 5
for i in range(depth, 0, -1):
    n = i
    for j in range(0, i):
        print(n, end=' ')
    print("\r")

#output like below pattern
#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5

row = 5
a = 0
for i in range(row, 0, -1):
    a += 1
    for j in range(1, i + 1):
        print(a, end=' ')
    print('\r')