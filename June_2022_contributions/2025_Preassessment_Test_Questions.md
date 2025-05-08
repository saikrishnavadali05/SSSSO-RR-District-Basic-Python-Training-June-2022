**2025 Python Training Pre-assessment MCQs** 

---

### **1. What is the output of the following code?**

```python
x = [i**2 for i in range(3)]
print(x)
```

A. `[1, 2, 3]`
B. `[0, 1, 4]`
C. `[0, 1, 2]`
D. `[1, 4, 9]`

**Answer:** B

---

### **2. What will be the output of this code?**

```python
def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))
```

A. `[1]` and `[2]`
B. `[1]` and `[1, 2]`
C. `[1]` and `[2, 1]`
D. `[1]` and `[2, 3]`

**Answer:** B

> **Note:** Default mutable arguments retain state across function calls.

---

### **3. What is the output of this code snippet?**

```python
a = 10
def change():
    a = 5
change()
print(a)
```

A. `5`
B. `10`
C. `Error`
D. `None`

**Answer:** B

> **Note:** `a` inside the function is local. The global `a` remains unchanged.

---

### **4. What will this code print?**

```python
x = [1, 2, 3]
y = x
x.append(4)
print(y)
```

A. `[1, 2, 3]`
B. `[1, 2, 3, 4]`
C. `Error`
D. `[4]`

**Answer:** B

> **Note:** `y` is a reference to `x`.

---

### **5. What does this lambda function return?**

```python
f = lambda x: x + 3 if x > 10 else x - 3
print(f(12), f(7))
```

A. `15 4`
B. `12 7`
C. `15 10`
D. `Error`

**Answer:** A

---

### **6. What is the result of this expression?**

```python
print(all([True, 1, "hello", []]))
```

A. `True`
B. `False`
C. `[]`
D. `Error`

**Answer:** B

> **Note:** `all()` returns `False` because an empty list `[]` is falsy.

---

### **7. What does the following code output?**

```python
x = "python"
print(x[::-1])
```

A. `python`
B. `nohtyp`
C. `Error`
D. `htonyp`

**Answer:** B

> **Note:** `[::-1]` reverses the string.

---

### **8. Which of the following statements is **true** about Python sets?**

A. Sets allow duplicate elements
B. Sets are ordered collections
C. Sets are immutable
D. Sets do not allow indexing

**Answer:** D

---

### **9. What will be the output of the following code?**

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c1 = make_counter()
print(c1(), c1(), c1())
```

A. `1 1 1`
B. `1 2 3`
C. `0 1 2`
D. `Error`

**Answer:** B

> Uses **closures** and `nonlocal` to retain `count` across function calls.

---

### **10. What does this decorator output?**

```python
def dec(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@dec
def greet(name):
    print(f"Hello {name}")

greet("Sai")
```

A. `Before Hello Sai After`
B. `Hello Sai`
C. `Before After Hello Sai`
D. `Hello Sai Before After`

**Answer:** A

> Shows how a **decorator** wraps a function call.

---

### **11. What is the output of the following code involving list mutation inside a function?**

```python
def func(x, y=[]):
    y.append(x)
    return y

a = func(1)
b = func(2)
c = func(3, [])
print(a, b, c)
```

A. `[1] [2] [3]`
B. `[1] [1, 2] [3]`
C. `[1, 2] [1, 2] [3]`
D. `[1, 2] [3] [3]`

**Answer:** B

> Shows **mutable default argument trap**. Same list reused across calls unless explicitly overridden.

---

### **12. What does this metaprogramming code print?**

```python
class A:
    pass

setattr(A, 'x', 100)
a = A()
print(a.x)
```

A. `Error`
B. `None`
C. `100`
D. `x`

**Answer:** C

> `setattr()` dynamically adds attribute `x` to class `A`.

---

### **13. What is the output of the following code?**

```python
def outer():
    x = 5
    def inner():
        print(x)
        x = 10
    inner()

outer()
```

A. `5`
B. `10`
C. `Error: local variable 'x' referenced before assignment`
D. `None`

**Answer:** C

> Python sees `x = 10` and treats `x` as a local variable, but it’s used before being assigned.

---

### **14. What will be the output of the following code?**

```python
print("Hello" * 3)
```

A. `Hello3`
B. `Hello Hello Hello`
C. `HelloHelloHello`
D. `Error`

**Answer:** C

---

### **15. Which of the following is used to handle exceptions in Python?**

A. `try...except`
B. `catch...throw`
C. `if...else`
D. `error...handle`

**Answer:** A

---

### **16. What is the output of this code?**

```python
a = [1, 2, 3]
b = a
a[0] = 0
print(b)
```

A. `[0, 2, 3]`
B. `[1, 2, 3]`
C. `Error`
D. `[0, 1, 2]`

**Answer:** A

> `b` references the same list as `a`.

---

### **17. Which of these is not a Python keyword?**

A. `pass`
B. `eval`
C. `assert`
D. `nonlocal`

**Answer:** B

> `eval` is a **built-in function**, not a keyword.

---

### **18. What will be the output of this code?**

```python
x = 10
def f():
    print(x)
f()
```

A. `10`
B. `Error`
C. `None`
D. `0`

**Answer:** A

> Accesses global `x` from within function.

---

### **19. What does `len([[]])` return?**

A. `0`
B. `1`
C. `2`
D. `None`

**Answer:** B

> It's a list containing one empty list.

---

### **20. Which data type is **immutable** in Python?**

A. `list`
B. `dict`
C. `set`
D. `tuple`

**Answer:** D

---

### **21. What is the output of this code?**

```python
print(10 // 3)
```

A. `3.33`
B. `3.0`
C. `3`
D. `3.3333`

**Answer:** C

> `//` is floor division.

---

### **22. Which of the following can be used to define an anonymous function in Python?**

A. `def`
B. `lambda`
C. `anon`
D. `func`

**Answer:** B

---

### **23. Which of the following statements about Python dictionaries is **true**?**

A. Dictionary keys can be duplicated.
B. Dictionary values must be unique.
C. Dictionary keys must be immutable.
D. Dictionary values must be strings.

**Answer:** C

---

### **24. What will be the output of the following code?**

```python
a = [1, 2, 3]
print(a[::-1])
```

A. `[1, 2, 3]`
B. `[3, 2, 1]`
C. `[2, 3, 1]`
D. `Error`

**Answer:** B

> `[::-1]` is used to reverse a list using slicing.

---

### **25. What will the following code output?**

```python
def add_items(item, target=[]):
    target.append(item)
    return target

print(add_items('A'))
print(add_items('B'))
```

A. `['A']` and `['B']`
B. `['A']` and `['A', 'B']`
C. `['B']` and `['A', 'B']`
D. `['A']` and `['B', 'A']`

**Answer:** B

> The default list `target` is **shared** across function calls.

---



