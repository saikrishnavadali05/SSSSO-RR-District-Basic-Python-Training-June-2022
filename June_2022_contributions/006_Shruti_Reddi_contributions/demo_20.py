#Write a program that accepts an integer (n) and computes the value of n+nn+nnn. If n is 5, the output should be 5+55+555 = 615

n=5
c=int(n)+int(n)*11+int(n)*111

print("5+55+555=", c)