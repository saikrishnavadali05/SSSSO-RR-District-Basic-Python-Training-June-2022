def add(a,b,c,d):
    return a+b+c+d
def multiply(a,b,c,d):
    return a*b*c*d
print("Select operation.")
print("1.Add\n2.Multiply")
while True:
    choice = input("Enter choice: ")
    if choice in ('1','2'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        

        if choice == '1':
            print(num1,"+",num2,"+",num3,"+",num4,"=",add(num1,num2,num3,num4))
        elif choice == '2':
            print(num1,"*",num2,"*",num3,"*",num4,"=",multiply(num1,num2,num3,num4))
        next_calculation = input("Let's do next calculation? : ")
        if next_calculation == "no":
          break

    else:
        print("Invalid Input")
