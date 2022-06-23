from audioop import avg
from statistics import mean


integer1 = float(input("Write number one: "))
integer2 = float(input("Write number two: "))
print("the highest number is:", max(integer1,integer2))
print("The lowest number is:", min(integer1,integer2))
a = (integer1 + integer2)/2
print("The average is:", a)
b = integer1 + integer2
print("The sum is: ", b)
c = integer1 * integer2
print("The product is: ",(integer1*integer2))