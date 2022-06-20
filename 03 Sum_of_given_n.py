#Write a program that accepts an integer (n) and 
# computes the value of n+nn+nnn. 
# If n is 5, the output should be 5+55+555 = 615
n = input("Enter the number:")
first = n
second = n+n
third = n+n+n
print("The given input is it after computing the n+nn+nnn result is",int(first) + int(second) + int(third))