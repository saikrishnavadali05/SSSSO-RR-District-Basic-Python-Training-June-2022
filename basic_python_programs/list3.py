data = ["a", 'b', 10, 3]
print(data)
print(data[1], data[1:-1])
print(data[:2], ['c', 3 * 1])

data[2:3] = [20, 30]    # change items
print(data)

data[2:4] = []          # remove items
print(data)

data[2:2] = [15, 18, 22]    # insert items
print(data)
print(len(data))

# nesting of lists
a = [10, 20, 12, 3]
b = [5, a, 30]
print(b, b[1])

a.sort()
print(a)

b[1].append(25)
print(b)