def add(Digits,Even):
    Sum = 0
    for i in range(0,Digits):
        Sum = int(Even[i]) + Sum
    print("The sum is",Sum)
