# Write a program to count number of digits in a number

# Non-Conventional method
number = int(input("Enter a number: "))
number = str(number)
print(number,"has",len(number),"digits in it.")


# Conventional method

# Note:
# Has an anomaly - When we enter zero(0) as input it prints zero digits as output

# count = 0
# while number != 0:
#     number //= 10
#     count += 1
# print(count)
