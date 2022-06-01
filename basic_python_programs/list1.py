e = [8, 15, 3, 20]

print("e1 = ", e)
e.append(-2)
print("e2 = ", e)

del e[2]
print("e3 = ", e)

f = e[1:3]              # array "slicing": elements 1 through 3-1 = 2
print("f = ", f)

print("e4 = ", e[1:])   # all elements starting with index 1

print("e5 = ", e[:2])   # all elements upto but excluding index 2

print("e6 = ", e[-1])   # means "1 item from the right end"

e.insert(2, 25)         # insert 25 at position 2
print("e7 = ", e) 

print("e8 = ", e[::2])   # all elements upto end in steps of 2

print(12 in e)          # tests for membership; true, false
print(20 in e)

# finds the index within the list of the given value
print("e9 = ", e.index(20))  

e.remove(20)      # If element is not found it returns valueError
print("e10 = ", e)
