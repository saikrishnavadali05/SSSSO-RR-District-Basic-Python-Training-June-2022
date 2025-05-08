#Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments (Hint : use argv)
#solution 1 using argv
import sys
program_name = sys.argv[0]
print('original list',program_name)
arguments = sys.argv[1:]
reversed_list = program_name[::-1]
#arguments = sys.argv[1:]
print('Updated List:',reversed_list)

