"""
15.Write a function calculate() such that it can accept two variables 
and calculate the addition, multiplication of them. 
The result must be returned a single return call. 
The two variables are lists. (Do arithmetic operations on lists).
"""
def calculate(var1,var2):
    s1 = 0
    p1 = 1
    s2 = 0
    p2 = 1
    for i in var1:
        s1+=int(i)
        p1*=int(i)
    for j in var2:
        s2+=int(i)
        p2 *= int(i)
    return "The first variable sum and mul is ",s1,p1 , "The second variable sum and mul is", s2,p2
v = [1,2,3,4,5]
v1 = [6,7,8,9,10] 

print(calculate(v,v1))
