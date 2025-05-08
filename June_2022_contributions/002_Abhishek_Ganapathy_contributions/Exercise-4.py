print("Question 1")
number1 = 20
number2 = 2
number3 = number1/number2
print("The division is", number3)

print("Question 2")
a = 5
b = 10
if a ** 2 > 50 and b < 50:
   print(a, b)
# No Answer is received since a**2 is 25 which is less than 50, hence the 1st conidtion is false and we do not have a else statement. For correct ans:
a = 5
b = 10
if a ** 2 > 50 and b < 50:
   print(a, b)
else:
    print("Have an else statement")

print("Question 3")
number = (45 - 3 ** 3) / 6
print(number)
# 3 (BODMAS Rule[(45-27)/6])

print("Question 4")
a = 2
b = 10
c = 6
a += b
b %=c
print(a, b)
print(c > b)
print(a == (a + b + c) - 20)
d = a < c or a != 12

print("Question 5")
print("----")
x = "kumari"
y = "ma"
print(y not in x)