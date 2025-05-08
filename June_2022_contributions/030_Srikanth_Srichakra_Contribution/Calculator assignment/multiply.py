def multiply():
    num = []
    mul = 1
    invalid = 0
    for i in range(0,4):
        temp = int(input("Enter number "+ str(i+1) + ": " ))
        num.append(temp)

    for i in num:
        if i%2 != 0:
            invalid += 1

    if invalid == 4:
        print("All numbers are odd, cannot perform multiplication.")
        return
    for i in num:
        if i%2 == 0:
            mul *= i    

    if invalid != 4:
        with open("output.txt", 'w') as f:
            f.write(str(mul))      