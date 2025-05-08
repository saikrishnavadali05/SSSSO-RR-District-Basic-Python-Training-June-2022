#Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)

a = int(input("Enter a number of your choice: "))
b = int(input("Enter another of your choice: "))

print("Minimum of %d and %d is '%d'"%(a, b,min(a,b)))


print("Maximum of %d and %d is '%d'"%(a, b, max(a,b)))

print("Average of %d and %d is '%f'"%(a, b,((a+b)/2)))

print("Sum of %d and %d is '%d'"%(a, b,a+b))


print("Product of %d and %d is '%d'"%(a, b,a*b))

print("difference of %d and %d is '%d'"%(a, b,a-b))
