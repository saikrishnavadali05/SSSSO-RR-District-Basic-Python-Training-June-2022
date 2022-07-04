try:
    a = int(input("Enter a number: "))
    b = int(input("enter another number: "))
    c = a / b
    print("Result of division is : ", c)

except Exception as  e:
    
    # User Defined Message
    print("Zero division is not posible")
    
    # Built in message
    print(e)