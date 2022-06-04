"""
Given a list of numbers. write a program to turn every item of a list 
into its square.

given

numbers = [1, 2, 3, 4, 5, 6, 7]

output

[1, 4, 9, 16, 25, 36, 49]

"""

#solution

numbers = [1, 2, 3, 4, 5, 6, 7]
# result list
res = []
for i in numbers:
    # calculate square and add to the result list
    res.append(i * i)
print(res)