import add
import multiply
l=input("enter numbers")
n1=l.split(" ")
n=[int(i) for i in n1]
even_numbers=[]
for i in n:
    if i%2==0:
        even_numbers.append(i)

if len(n)==len(even_numbers):
    print("sum is ",add.add(n))
    print("multiplication is",multiply.multiply(n))
elif len(n)<4:
    print("Enter 4 numbers") 
else:
    print("enter only even numbers for calculation")  

