from email.errors import MultipartInvariantViolationDefect


current = 90
resistance = 40
voltage = current * resistance
print("The given current is", current, "and resistance is", resistance, "So the total voltage flows in the circuit is", voltage, "V")
#Assignment Operator
N = 50
M = 5
N += M
print("The addition is- ", N)
N = N*M
print("The Product is- ",N)
N = N**M
print("THe exponential power is -", N)
N /= M
print("the division is -", N)
N = N//M
print(N)
#Excercise 4
#1
print(20 / 2)
#2
print("the answer is - B")
#3
nubb = (45- 3 ** 3)/6
print(nubb)
#4
a = 2
b = 10
c = 6
a += b
b %=c
print(a, b)
print(c > b)
print(a == (a + b + c) - 20)
d = a < c or a != 12
print(d)

#5
x = "kumari"
y = "ma"
print(y in x)