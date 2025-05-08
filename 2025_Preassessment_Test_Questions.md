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
