from addition import add
n= 4
lst = []
num1 = int(input("enter the 1st number"))
num2 = int(input("enter the 2nd number"))
num3 = int(input("enter the 3rd number"))
num4 = int(input("enter the 4th number"))

lst.insert(0,num1)
lst.insert(1,num2)
lst.insert(2,num3)
lst.insert(3,num4)
result = 0
temp = 1
for num in lst:
 
   
    if num % 2 == 0:
        result = num + result
    
print("given numbers are odd numbers")
print(result)

for num in lst:  
    if num % 2 == 0:
       
        temp = num * temp 
        
        
print(result)



