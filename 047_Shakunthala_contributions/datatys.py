print("sai ram")
a = 24
b = 35.2
c = 2 +3j
m = float(a) #convert from int to floa
n = complex(a) #convert from int to complex
o = int(b) #convert from float to int:
p = complex(b) #convert from float to complex
print(m)  #24.0
print(n)  #(24+0j)
print(o)  #35
print(p)  #(35.2+0j)
 

number1 = 24
number2 = 35

#arithmetic operations

add = number1 + number2 
sub = number1 - number2  
multiply = number1 * number2
div = number1 / number2
expo = number1 ** number2 

print("The results are") 
print("addition ", add) # 59
print("substraction ", sub) #-11
print("multiply ", multiply) #840 
print("division ", div) #0.68571428
print("exponentation ", expo) #202952058160
 
#Frozen set

Student = {"name": "akhil", "age": 21, "sex": "male"}
y=frozenset(Student)
print('frozen set',y) #frozen set frozenset({'sex', 'age', 'name'})

#Commands line arguments 
from sys import argv

print("argvlist:",argv)

p = int(argv[1])
x = int(argv[2])
y = int(argv[3])
z = int(argv[4])
addition1 = p + x  
addition2 = y + z                            
print("addition1 result is", addition1)    
print("addition2 result is", addition2)

#output
#argvlist: ['datatys.py', '10', '20', '30', '40']
#addition1 result is 30
#addition2 result is 70     
