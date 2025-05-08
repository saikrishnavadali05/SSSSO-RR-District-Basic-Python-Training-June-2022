def add(a, b , c, d):
    return a + b + c + d
def multiply(a, b , c , d):
    return a * b * c * d
print("Select the below given operations.")
print("1.Addition")
print("2.Multiplication")
while True:
    choice = input("Enter choice(1/2): ")
    if choice in ('1', '2'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))

        if choice == '1':
            print(num1, "+", num2,"+",num3,"+",num4, "=", add(num1, num2,num3,num4))

        elif choice == '2':
            print(num1, "*", num2,"*",num3,"*",num4, "=", multiply(num1, num2,num3,num4))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
