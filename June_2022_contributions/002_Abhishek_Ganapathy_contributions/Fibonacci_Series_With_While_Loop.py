Fibonacci = [0,1]
i = int(input("Enter the Fibonacci "))
n = 3
while n < i + 1:
    value = Fibonacci[n - 2] + Fibonacci[n - 3]
    Fibonacci.append(value)
    n = n+1
print(Fibonacci)
    
