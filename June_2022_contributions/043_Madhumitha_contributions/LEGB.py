#LEGB- Local, Enclosed, Global, Built-in

#Global
value=10

def illustrtion():
    #local
    value = 20
    print("value inside function : ",value)
    return value

print("value outside function : ",value)
return_val = illustrtion()
print(return_val)
print("value outside function : ",value)
