#Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments (
a=list(map(int,input("enter elements with space ").split()))
print("reverse order is ",end="")
for i in range(len(a)):
    print(a[len(a)-i-1],end=" ")
