# Exercise-10

# Write a function that take string as a parameter.the string is given by the user as input.the final output from the function is to reverse the string.
def reverse_string(string):
    return string[::-1]

user_string = input("Enter a valid string: ")
rev_str = reverse_string(user_string)
print("Reversed string is", rev_str)


# Write a function that take three integers and compare which the largest and smallest among the them. take input from the end user.
def largest_smallest(a,b,c):
    if a>b and a>c:
        print(a,"is the largest.")    
    elif b>a and b>c:
        print(b,"is the largest.")
    else:
        print(c,"is the largest")
    
    if a<b and a<c:
        print(a,"is the smallest.")    
    elif b<a and b<c:
        print(b,"is the smallest.")
    else:
        print(c,"is the smallest")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
largest_smallest(a,b,c)