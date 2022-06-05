# Program to demonstrate various data types


variable_demo = 3 + 4 + 5 + 6 + 7 + 8 + 3 + 4 + 5 + 6 + 7 + \
8 + 3 + 4 + 5 + 6 + 7 + 8 + 3 + 4 + 5 + 6 + 7 + 8 + 3 + \
4 + 5 + 6 + 7 + 8 + 3 + 4 + 5 + 6 + 7 + 8

print(variable_demo)

variable_demo = 55  + 35

print(variable_demo)

variable_demo = 55 - 35

print(variable_demo)

variable_demo = 55 / 35

print(variable_demo)

variable_demo = "sai krishna"

print(variable_demo)

variable_demo = 9.354

print(variable_demo)

#mutable datatype - list
variable_demo = [1, 2, 3, 4]

print(variable_demo)

# immutable - string
variable_demo = ";slfgasf;hg;ashg;"

print(variable_demo)

variable_demo = True

print(variable_demo)

variable_demo = False

print(variable_demo)

#immutable datatype - tuple
tuple_demo = (2, 3)

print(tuple_demo)

dictionary_demo = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",
    "key4" : "value4",
}

print(dictionary_demo["key1"])
print(dictionary_demo["key3"])

#mutable
set_demo = {1, 2, 3, 3, 4, 4, 1, 100, 2, 5, 5}

print(set_demo)

a = 3+7j
b = 5-9j

print(a+b)

## type casting

a = 34
b = 36.5 
c = 2 +5j   
                            
m = float(a) #convert from int to float 
n = complex(a) #convert from int to complex 
o = int(b) #convert from float to int:
p = complex(b) #convert from float to complex 

print(m)
print(n)
print(o)
print(p)

a = "10asdlkgbsdg"
print(a)

a = "10lsdhlgsa"
print(a)

string = "water_bottle"
# string[5] = '.'
print(string)

new_string = string[:5] + '.' + string[6:]
print(new_string)