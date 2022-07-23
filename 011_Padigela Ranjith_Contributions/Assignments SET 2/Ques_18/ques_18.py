"""
18.Write a script to read last n lines of a file. 
Accept filename and n as input from the user. Similar to Unix tail command. 
(understand how unix tail command works by searching on google or youtube).
"""

def lastnlns(fname,N):
    with open(fname) as file:
        for i in (file.readlines()  [-N:]):
            print(i,end=" ")

if __name__ == '__main__':
    fname = 'mypar.txt'
    N = int(input("Enter the number here: "))
    try:
        lastnlns(fname,N)
    except:
        print('file is not found')