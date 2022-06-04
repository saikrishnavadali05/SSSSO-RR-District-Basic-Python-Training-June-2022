"""
given an integer n print the number. Print the list of integers without spaces.


Examples
n = 3
output should be
123

n = 6
output should be
123456



"""

if __name__ == '__main__':
    n = int(input())
    #fill the code


#Solution

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1,1):
        print(i, end="")
