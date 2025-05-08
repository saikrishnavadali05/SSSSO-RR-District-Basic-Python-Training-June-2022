#1. Write a program to build a calculator. The calculator should be able to read 4 numbers and print the addition and multiplication of ONLY THE EVEN numbers using functions. 
#solution
n1,n2,n3,n4=list(map(int,input("enter 4 integers:").split()))
print(n1,n2,n3,n4)
def add():
    print("add file is active")
total=0
for number in n1,n2,n3,n4:
    if(number%2==0):
        print("{0}".format(number))
        total=total+number
        print("The sum of even number is ={1}".format(number,total))
else:
    print("You have entered some  odd number Please entered even numbers of your choice")
#solution
n1,n2,n3,n4=list(map(int,input("enter 4 integers:").split()))
print(n1,n2,n3,n4)
def add():
    print("add file is active")
to=1
for number in n1,n2,n3,n4:
    if(number%2==0):
        print("{0}".format(number))
        to=to*number
        print("The multiple  of even number is ={1}".format(number,to))
else:
    print("You have entered some  odd number Please entered even numbers of your choice")

#solution
def calculator(add,multiple):
    with open (add,"r") as rnf:
        exec(rnf.read())
    with open (multiple,"r") as rmf:
        exec(rnf.read())
a=input("enter your choice of add or multiple",add,multiple)