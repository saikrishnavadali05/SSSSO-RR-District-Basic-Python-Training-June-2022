a = 5
b = 10
[a, b] = [b, a]   # Elegant way to swap two variables
print("a = ", a, "b = ", b)

# Multidimensional lists can be implemented as lists
c = []
c.append([1, 2])
print("c = ", c)
c.append([3, 4])
print("c1 = ", c)

x = 4 * [2]
print("x = ", x);

y = 3 * [x]     # [[2,2,2,2],[2,2,2,2],[2,2,2,2]]
print("y = ", y);
print("y1 ", y[0][2])

print(id(y[0]))
print(id(y[1]))
print(id(y[2]))

y[0][2] = 1
print("y2 ", y)
