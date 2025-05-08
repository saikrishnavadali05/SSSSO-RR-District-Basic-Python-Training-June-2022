def Add(Digit,Even):
    add = 0
    for i in range(0,Digit):
        add = int(Even[i]) + add
    print("The sum is",add)
