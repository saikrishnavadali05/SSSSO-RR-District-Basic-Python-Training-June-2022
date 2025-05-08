# Demonstrating Lambda in Python

sum = lambda a,b :  a+b

sub = lambda a,b : a-b

mul = lambda a,b : a*b

div = lambda a,b : a/b

exp = lambda a,b : a**b

print(sum(10,20))
print(sub(100,30))
print(mul(3,2))
print(div(22,7))
print(exp(11,2))

# Lambda function inside a regular function

def fun(n):
    return lambda a : a * n

triple = fun(3)
print(triple(11)) # 33


