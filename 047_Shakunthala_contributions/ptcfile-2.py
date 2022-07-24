#Assignment operators
x = 20
y = 30
x = x + y
print(x)               #50
x = x - y              #20
print(x)               #600
x = x * y              #221073919720
print(x)               #72.369130657
x = x ** y             #24.45637688578
print(x)               #0.0
x/= y
print(x)
x //= y
print(x)
x %= y
print(x)

#Escape sequences
# using \b,\n,\t,\r,\a,\\,"\",'\'

txt = "ram is \"very good\" boy" # ram is "very good" boy
print(txt)                       # Hello
X = "Hello\nworld"               # world
print(X)                         # world
Y = "Hello\rworld"
print(Y)

#Conditional statements

number = int(input("Enter the number "))
if number > 0:
    print("greater than zero")    
else:
    print("zero")
#Enter the number 2
#greater than zero                         

# Loops
 
i=0
while i<5:                  # 1 Hello
    print(i,'Hello')         # 2 Hello
    i=i+1                     #3 Hello
                              # 4 Hello
                              # 5 Hello
str= "Hello world"            
for i in str:          
    print(i)               
    #H
    #e
    #l
    #l
    #o
    #w
    #o
    #l
    #d
    