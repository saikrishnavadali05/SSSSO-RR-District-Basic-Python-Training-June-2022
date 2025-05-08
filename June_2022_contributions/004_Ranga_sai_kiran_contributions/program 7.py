def diamond(n):
    for m in range(0, n):
        for i in range(0, m+1):
            print("* ",end="")
print("\r")
n = 5
diamond(n)