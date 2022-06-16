# SSSSO-RR-District-Basic-Python-Training-June-2022

Basic Python Training Organized by Sri Sathya Sai Seva Organization RR District in the month of June 2022.

## Timings

1. Saturday - Evening - 6pm to 8pm
2. Sunday - Morning - 8am to 10am

> Total - 4 hours of training sessions per week

## Rewards
> Top 10 Contributors to this Repository will get a Merit Certificate and Special Rewards from the SSSSO RR District Python Training Organizers

# Setting up git and github, python 3.10, VS Code

1. [programming knowledge channel - How to Install Git on Windows 10 + Setting Up Git and GitHub on Windows 10](https://www.youtube.com/watch?v=bb_LoXAC-zE)
2. [How to install python 3.10 on windows 10/11](https://www.youtube.com/watch?v=AwIXfaGEN4c)
3. [How to install visual studio code on windows 10/11](https://www.youtube.com/watch?v=JPZsB_6yHVo)

## List of Topics that will be covered under this training <a name="top"></a>

1. [Let's begin the Python Show](#1)
   - [History of Python](#1.1)
   - [What is Python](#1.2)
   - [Applications of Python](#1.3)
   - [How does Python Programming Language support a Complex Problem Decomposition](#1.4)
   - [What is an interpreter](#1.5)
   - [How To Open and Run the Interpreter Which is installed](#1.6)
   - [Comparison of python with other Languages](#1.7)
   - [Famous and Most used versions of python](#1.8)
   - [Why should we learn Python](#1.9)
2. [About Python](#2)
   - [Writing python scripts in a file and running it in the command line
     interface](#2.1)
   - [Commenting in python](#2.2)
   - [Print function](#2.3)
   - [Header for Python script](#2.4)
   - [Indentation](#2.5)
   - [Continuation lines](#2.6)
3. [Data Types](#3)
   - [Integers](#3.1)
   - [Floating point](#3.2)
   - [Complex](#3.3)
   - [boolean](#3.4)
   - [frozen sets](#3.5)
   - [Conversion of one data type to another](#3.6)
   - [Exercise - 1](#3.7)
4. [Variables](#4)
   - [Python Variables](#4.1)
   - [Common conventions followed for variable names](#4.2)
   - [Creating good names](#4.3)
   - [Exercise - 2](#4.4)
5. [User Input](#5)
   - [Input function](#5.1)
   - [Command line parameters (arguments)](#5.2)
   - [Exercise - 3](#5.3)
6. [Operators](#6)
   - [Numeric](#6.1)
   - [Assignment](#6.2)
   - [Comparision](#6.3)
   - [Logical](#6.4)
   - [Membership](#6.5)
   - [Identity](#6.6)
   - [Bitwise](#6.7)
   - [Exercise - 4](#6.8)
7. [strings](#7)
   - [Indexing](#7.1)
   - [Object Identity](#7.2)
   - [Program using builtin function](#7.3)
   - [Formatting with .format method](#7.4)
   - [Important points to remember](#7.5)
   - [builtin functions, methods of string](#7.6)
   - [Slicing Operator in Lists and Strings](#7.7)
   - [Exercise - 5](#7.8)
8. [Escape sequences](#8)
   - '\n' - [Newline character](#8)
   - '\r' - [Return character](#8)
   - '\b' - [Backspace character](#8)
   - '\\' - [Backslash character](#8)
   - '\”' - [Double quote character](#8)
   - '\’' - [Single quote character](#8)
   - '\t' - [Tab character](#8)
   - '\a' - [Alarm character](#8)
   - [Exercise - 6](#8.1)
9. [Conditional statements](#9)
   - [If](#9.1)
   - [If else](#9.2)
   - [Nested If elif else](#9.3)
   - [Exercise - 7](#9.4)
10. [Loops](#10)
    - [While](#10.1)
    - [for](#10.2)
    - [Exercise - 8](#10.3)
11. [Lists](#11)	
12. [range function](#12)
    - [Exercise - 9](#12.1)
13. [Tuples](#13)
    - [Exercise - 10](#13.1)
14. [Sets](#14)
    - [Exercise - 11](#14.1)
15. [Dictionaries](#15)
    - [OrderedDict module](#15.1)
    - [Exercise - 12](#15.2)
16. [Functions](#16)
    - [Exercise - 13](#16.1)
17. [Modules](#17)
    - [Standard Modules](#17.1)
18. [Namespaces](#18)
19. [Packages](#19)
20. [File Handling](#20)
    - [Read](#20.1)
    - [Write](#20.2)
    - [delete](#20.3)
    - [Important functions and points for file handling](#20.4)
    - [Exercise - 14](#20.5)
21. [Exception Handling](#21)
    - [Exercise-15](#21.1)
22. [Built in tools](#22)

## Answers <a name="answers"></a>

1. [Exercise - 1](#E-1)
2. [Exercise - 2](#E-2)
3. [Exercise - 3](#E-3)
4. [Exercise - 4](#E-4)
5. [Exercise - 5](#E-5)
6. [Exercise - 6](#E-6)

## **1. Let's begin the Python Show** <a name="1"></a>

### **History of Python** <a name="1.1"></a>

**Python** was developed by **_Guido van Rossum_** and was released first on **February 20, 1991** (31 years ago). It is one of the most widely-used and loved programming languages. It is also a **free** and **open-source language** with very simple and clean syntax.

### **What is Python?** <a name="1.2"></a>

1. **Python** is a **general-purpose high-level** programming language. Being a general-purpose language, it can be used to build almost any type of application with the right **tools** or **libraries**.
2. Its standard library is large and comprehensive. This makes it easy for **developers** to learn python.
3. Additionally, python supports **objects**, **modules**, **threads**, **exception-handling**, and **automatic memory management** which will help in modeling real-world problems and building applications to solve those problems.
4. Python is widely used among the latest and most emerging fields such as **Machine Learning**, **Deep Learning**, **Artificial Intelligence**, **Web Development**, **Web Scraping**, **Data Mining**, **Data Visualization**, **Data Science** and various other trending domains.

### **Applications of Python?** <a name="1.3"></a>

**Python** has grown to become an integral part of most of the recent web-based, desktop-based, graphic design, scientific, and computational applications. **The following are just a few applications of the enormous python language**. The List goes on and goes, as we keep exploring more and more fields, where python is used extensively.

- GUI based desktop applications

  > Tkinter, PyQT, Kivy, WxPython, PyGUI these are most widely used and best Python graphical user interface frameworks available.

- Graphic design, image processing applications, Games.
  > OpenCV, Pillow, SimpleITK are some libraries of image processing .
- Web frameworks and applications.

  > Django, Flask, TurboGears, web2py and some other Python web framework are used for Python Web development.

- Business applications

  > Python is also used to build ERP and e-commerce systems like Oodo, Tryton, OpenERP.

- Operating Systems

  > Linux, FreeBSD, Windows, macOS are the operating systems.

- Database Access

  > MySQL, PostgreSQL, MongoDB are some database servers used by Python.

- Scientific and Numeric

  > Python has many libraries for scientific and numeric such as Numpy, Pandas, Scipy, Scikit-learn, etc.

- Prototyping

  > Developers can quickly write test/validation code which gives the expected results for small to medium data sets.

- Software Development
  > Scons, Buildbot, Apache Gump, Round up, Trac.

<br />

[go to List of Topics](#top)

<br />

### **How does Python Programming Language support a Complex Problem Decomposition?** <a name="1.4"></a>

1. **Python** supports **multiple** programming paradigms and features a fully dynamic type system and automatic memory management, similar to Perl, Tcl etc. Like other dynamic languages. Python is often used as a **scripting language**.
2. If you have to work with several C libraries, and the usual is order of C is

   > write code -> compile it -> test it -> re-write -> re-compile the code -> re-test.

   - So, The cycle is slow. You need to develop **software** more quickly. Possibly, perhaps you have written a program that could use an **extension language**, and you do not want to design a language, write and debug an interpreter for it, then tie it into your application.

3. **Python** allows you to split up your big program (program with many lines of code) into modules that can be **reused**, even into other Python programs as well. It comes with a **large collection** of standard modules that you can use as the basis of your programs, instead of writing code for each and everything from scratch.
4. There are also built-in modules that provide things like file I/O, system calls, sockets, and even interfaces to graphical user interface toolkits like Tk.

<br />

### **What is an interpreter?** <a name="1.5"></a>

1. An **interpreter** is a program that reads and executes code line-by-line. This includes source code, pre-compiled code, and scripts.
2. Common interpreters include Perl, Python, and Ruby interpreters, which execute Perl, Python, and Ruby code respectively.
3. If we write a Python code in a text file with a name like hello.py. How does that code Run? There is a program installed on your computer named "python3" or "python", and its job is to look at and run your Python code. This type of program is called an "interpreter".

<br />

### **How To Open and Run the Interpreter which was installed?** <a name="1.6"></a>

1. There are 2 easy ways to open the interpreter:

   - Open a command-line terminal or command prompt.
   - **Mac** : run the "Terminal" app in the Utilities folder.
   - **Windows**: Type "Command Prompt" in the search box, this opens the Windows command prompt terminal. In the terminal, type the command "python3" or "python" or sometimes "py". This runs the interpreter program directly.
   - press `ctrl+d` or `ctrl+z` or `type exit()` to exit the interpreter.

     - If you have **Visual Studio Code** installed, at the top of the VS Code window, click on the **Terminal** option. And then click on the **New Terminal** option.

   - > In Visual Studio Code : Terminal > New Terminal

2. When commands are read from a **tty**, the interpreter is said to be in **interactive** mode. In this mode it prompts for the next command with the primary prompt, usually three greater-than signs **(‘>>> ‘)**. `>>>` this symbol is called as `chevron prompt`. It means that python interpreter is in `interactive mode`, waiting for user input.

3. For continuation lines it prompts with the secondary prompt, by default three dots **(‘...’)**. The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt. The symbol `...` in this context, should not be compared (or) correlated with `... <ellipsis>` operator of python.

4. Continuation lines are needed when entering a multi-line construct. As an example, look at this if statement:

![](https://github.com/saikrishnavadali05/python3_ebook/blob/master/Images/Screenshot%202022-01-31%20110438.jpg?raw=true)

### **Comparison of python with other Languages?** <a name="1.7"></a>

| Column                                          |     Python     |      Java |      C++       |              C |
| :---------------------------------------------- | :------------: | --------: | :------------: | -------------: |
| Code Executor                                   |  Interpreter   |  Compiler |    Compiler    |       Compiler |
| Learning and Coding Difficulty Level            |   Very Easy    |    Medium |     Medium     |      Difficult |
| Number of Lines of Code (SLOC)                  |   Very less    |      Less |      Many      | Extremely Many |
| Costs incurred to Build Applications            | Less Expensive | Expensive | More expensive | Most expensive |
| Availability of Learning and Reusable Resources |   Very High    |      High |      Less      |           Less |

<br />

[go to List of Topics](#top)

<br />
 
### **Famous and Most used versions of python?** <a name="1.8"></a>

There are multiple versions of python since its inception.
Out of which, versions after `Python 3.4 ` are the most widely used ones.

1. 1989, Implementation of Python as a successor of `ABC Programming Language` started.
2. 1991, Python 0.9
3. 1994, Python 1.0
4. 2000, Python 2.0 (was popular, but no longer supported since Jan 1, 2020).
5. 2008, Python 3.0 (Famous)
6. 2022, Python 3.10 (Very Very Famous and Huge Developer Community)

- The main difference between version 2 and version 3 is **the stablity of the code has increased a lot** and there were a few changes in the syntax and also increase in **speed of execution of code**. So, Now version 2 has no support or resources so everyone should have latest version in their Local system.

 <br />

### **Why should we learn Python?** <a name="1.9"></a>

1.  By the **start** of 2022 :
    **PyPi** (Python Package Index) has > **3,50,000** Python packages (almost all of them are free and open source).
    10 million+ (1 crore+) python developers are flourishing all around the world (Huge python developer community).

2.  In the mid of 2021 :
    **6,200** companies (around the world) have used (90% of their code is written only in) Python for their platforms.
    **10,000+** Python job ads on **Glassdoor**.
    **14,000+** Python openings on **Indeed**.

3.  The number might have **doubled** by now (i.e., June 2022).

4.  A Rapid growth is being observed in the world of Python.
    Because, Python is **very easy to read, write and understand**.
    Learning Python is not as difficult as it looks, but it’s definitely **worth your efforts**.

5.  In #india, python developers are being paid well... What is the reason?

        4.27 lpa ----> 9.09 lpa ----> 11.5 lpa

6.  The following are the average salaries based on different **experience** levels

    - The average salary of an **_entry-level_** Py developer - **\*₹427,293\*\***.
    - The average salary of a **_mid-level_** Py developer - **_₹909,818_**.
    - The average salary of an **_experienced_** Py developer - **_₹1,150,000_**.

7.  _The reason is simple and straight forward_. Many of the top companies use python extensively. The following list contains, but not limited to only software companies. In fact, python is being used even by Bio-scientists, Chemical Scientists, etc..

8.  Examples of companies that use Python extensively are

> Top Financial Companies

- Goldman Sachs
- JP Morgan Chase
- PayPal

> Large Tech Companies

- Google #google
- Dropbox #dropbox
- Netflix #netflix
- Meta #Meta (Facebook), #instagram
- Uber
- Twilio
- Mozilla
- Reddit
- Increment

> US Government Agencies

- The Consumer Financial Protection Bureau (CFPB)
- NASA
- United States Central Intelligence Agency (CIA)
- Securities and Exchange Commission (US SEC)
- Department of the Navy and National Institute of Standards and Technology (NIST)

> Important Multi National Companies that use python extensively

- Nokia, HPE, Dell, Novell, emc2, vmware, mindtree, OLA, Persistent, GSLabs, Macropace, Xentrix, etc

The list goes on and on... all of them use python extensively.
Python programmers are very high in demand now-a-days..

> One easy way to become rich in the software industry is to learn and perform : **web development using python**.

9. Web Development using Python :

- Python
- Django / Flask
- HTML
- CSS
- JavaScript

The best and most productive field to flourish today is **web development** using python. Which is also popularly known as **Full Stack Python**

<br />

[go to List of Topics](#top)

<br />

## **About Python** <a name="2"></a>

### **python scripts and its execution** <a name="2.1"></a>

1. A computer program is a sequence of instructions in a programming language that a computer can execute or interpret.
2. The basic difference between a **scripting language** and other general purpose programming languages such as C, C++, JAVA is that scripting languages do not need an additional step of compilation and rather they are interpreted, whereas programming languages are compiled and hence need a compilation step to convert the high-level language to machine code.
3. Scripting Languages are mainly written to automate many tasks with as less code as possible.
4. Scripting languages support "script," which is small program written for a specific runtime environment. These are interpreted at runtime rather than compiled.
5. The scripts of python are written in a file and must be saved with an extension .py. Then, at the time of execution, the python interpreter can understand that it is running the python file.
6. The scripting language refers to dynamic high-level, general-purpose interpreted languages such as Python, Perl, etc.
7. for executing the python file the command is **python filename.py**
8. Example - The script present in python file

```python
   print("I like learning Python Language")
```

execution of the python file
<img src="https://github.com/Vissamsetty-Bharathrath/python3_ebook/blob/master/Training/17.jpg" alt="python scripts and its execution" width="600"/>

  <br />
  
  ### **Commenting in python** <a name="2.2"></a>
  
  1. **Comments** are text portions that clarify what the program does and how it functions. 
  2. The character used for commenting is ```#```.
  3. The Python interpreter ignores the following text from where the character ```#``` starts.
  4. Example
  ```python
      # print("I like learning Python Language")
  ```
  ```python
  #This is a comment
  #written in
  #more than just one line
  print("Hello, World!")
  ```
  
  ```console
  #output
  Hello, World!
  ```
  
  ```python
  '''
  This is a comment
  written in
  more than just one line
  
  Multiline comment
  '''
  print("Hello, World!")
  ```
 
   ```console
  #output
  Hello, World!
  ```
  
 <br />

### **Print function** <a name="2.3"></a>

1. This is the basic function which is used to print the content on the screen. This function always give a **new line**
2. Syntax for the **print** function
   > print (objects, sep = ':', end = '\n')
   - objects can be more than one.
   - Here, **sep** and **end** are **optional**. **sep** is used to seperate objects and **end** is used to tell what it should do at the end of statement.
3. Examples of the print function are

   ```python
     print("My name is Ramesh", "studying in IIT")
   ```

   - From the above print statement "My name is Ramesh" is expression -1 and "studying in IIT" expression -2.
   - Prints the expressions with spaces between them

     ```python
        print("My name is Ramesh", "studying in IIT", sep=':', end=' ')
     ```

   - Prints the expressions with : between them and also new line is avoided from end.

4. After executing the two print statement examples the answers are
   <img src="https://github.com/Vissamsetty-Bharathrath/python3_ebook/blob/master/Training/19.jpg" alt="Print function" width="600"/>

 <br />
   
 [go to List of Topics](#top)

<br />
   
 ### **Header for Python script** <a name="2.4"></a>
  
  1. The **header** is very important for the program because when anybody wants to understand your program or if you want to revise this program in the future the header will be very helpful to tell how **code works**.
  
```python
#(**/*+-(**/*+-(**/*+-(**/*+-(**/*+-(**/*+-(**/*+-    % PYTHON %    (**/*+-(**/*+-(**/*+-(**/*+-(**/*+-(**/*+-
#
#
#
# Python Training - Chapter - 3 - Exercise 4 - Question -1 
#
# Description:
#  The code takes two integers and do arithmetic operations on the integers.
# 
#
# Usage:
#  python addition.py 
#
#
#(**/*+-(**/*+-(**/*+-(**/*+-(**/*+-(**/*+-(**/*+-    % PYTHON %    (**/*+-(**/*+-(**/*+-(**/*+-(**/*+-(**/*+-

#user input

number1 = int(input("Give first number "))
number2 = int(input("Give second number "))

#arithmetic operations

add = number1 + number2
sub = number1 - number2
multiply = number1 \* number2
div = number1 / number2
expo = number1 \*\* number2

print("The results are")
print("addition ", add)
print("substraction ", sub)
print("multiply ", multiply)
print("division ", div)
print("exponentation ", expo)

````

* running script
> PS C:\Users\Documents\Training\code> python operations.py

```console
# output

Give first number 12
Give second number 2

The results are
addition  14
substraction  10
multiply  24
division  6.0
exponentation  144
````

<br />
   
### **Indentation** <a name="2.5"></a>

1. **Indentation** plays a very important role in writing **python script**.
2. The meaning of indentation is the proper **arranging** of the lines of code in the script.
3. For arranging we can either use **Tab** or **Space**. But the right way is to use Tab which makes our code to write easily.
4. Now let's understand with an example

```python
# Convert the command line parameters (arguments) to numbers
num1 = 7
num2 = 10

# Determine which number is largest and perform the subtraction
if num1 > num2:
  diff = num1 - num2
  print(num1, "-", num2, "=", diff)
else:
  diff = num2 - num1
  print(num2, "-", num1, "=", diff)
```

- running script
  > PS C:\Users\Documents\Training\code> python indentation.py

```console
# output

10 - 7 = 3
```

From the above example, we can see there is a white space after the `if` line it is given because the lines should be executed only when the `If` condition satisfies. Similarly for the 'else' condition.

<br />
  
 ### **Continuation lines** <a name="2.6"></a>
 
  1. If we are writing one big statement that occupies more than one line then we will be using this character ```\```. 
  2. This character ```\``` should be the end of the line.
  3. For example 
   ```python
     print("My company \
     name is \
     Multiple Wishes.")
   ```
   when we run the script the output is
   <img src="https://github.com/Vissamsetty-Bharathrath/python3_ebook/blob/master/Training/11.jpg" alt="Continuation lines" width="600"/>

<br />

[go to List of Topics](#top)

<br />

## **Data Types** <a name="3"></a>

1. **Variables** can hold values, and every value has a data-type.
2. **Data-types** in Python can be either mutable or immutable.
3. A **mutable** object can be changed after it is created, and an **immutable** object cannot. Objects of built-in types like (int, float, bool, str, tuple, frozenset) are immutable. Objects of built-in types like (list, set, dict) are mutable. Custom classes are generally mutable.

| Class     | Description                      | Immutable |
| --------- | -------------------------------- | --------- |
| bool      | Boolean value                    | Yes       |
| int       | Integer                          | Yes       |
| float     | Float point number               | Yes       |
| list      | Mutable sequence of objects      | No        |
| tuple     | Immutable sequence of objects    | Yes       |
| str       | Character string                 | Yes       |
| dict      | Associative mapping (dictionary) | No        |
| set       | Unique set of values             | No        |
| frozenset | Immutable form of set            | Yes       |

<br />
  
### **Integer data type** <a name="3.1"></a>

1. The **integer** data type has only numbers without decimals in it. The numbers are either positive or negative.
2. Examples:

```python
    No_of_wickets = 5
    overs_bowled = 4
```

<br />

### **Floating-point data type** <a name="3.2"></a>

1. The **floating** point data is the having decimal point after integers.
2. 2. Examples:

```python
strike_rate_of_batsman = 105.45
economy_of_bowler = 6.25
```

3. we can also represent the floating point with **e** or **E**. **e** **E** means is the power of 10.

```python
strike_rate_of_batsman = 80e5
economy_of_bowler = 24E3
overs_bowled = 4.3
```

- After we print the above variables the answers are
  <img src="https://github.com/Vissamsetty-Bharathrath/python3_ebook/blob/master/Training/21.jpg" alt="Floating_data_type" width="500"/>

<br />

### **Complex data type** <a name="3.3"></a>

1. The **complex** data type is has an imaginary part in it. The imaginary part is represent with **j**.
2. Examples

```python
a = 3+7j
b = 5-9j
```

 <br />
 
### **Boolean data type** <a name="3.4"></a>

1. It has two values **True** and **False**
2. Examples

```python
ram_age = 25
shyam_age = 12
print(ram_age > shyam_age)
print(ram_age < shyam_age)
```

```console
Output :
True
False
```

<br />

### **Frozen sets** <a name="3.5"></a>

1. The method `frozenset`  in Python takes an iterable object as input and renders it immutable. Simply put, it renders iterable things unchangeable by freezing them.
2. In Python, a `frozenset` is the same as a set, except that frozensets are immutable, which implies that once generated, elements from the frozenset cannot be added or deleted.
3. This method accepts any iterable object as input and turns it to an immutable object. The element order is not guaranteed to be kept.

```python
person = {"name": "Ram", "age": 21, "sex": "male"}

f_Set = frozenset(person)
print('The frozen set', f_Set)
```

```console
# output
The frozen set is: frozenset({'name', 'sex', 'age'})

```

use of  dictionary as an iterable for frozen set, the set is created using just the dictionary's keys.

```python
# converting a list into a frozenset using the frozenset() function.

list = ['sai', 'ram', 'shyam']
y = frozenset(list)
print(y)
```

```console
# output

frozenset({'sai', 'ram', 'shyam'})
```

<br />

### **Conversion of one data type to another** <a name="3.6"></a>

1. We can **convert** from int to float, int to complex, float to int, float to complex.
2. We can not convert the complex to int or float data types.
3. Examples

```python
a = 34
b = 36.5
c = 2 +5j

m = float(a) #convert from int to float
n = complex(a) #convert from int to complex
o = int(b) #convert from float to int:
p = complex(b) #convert from float to complex

output
34.0
(34+0j)
36
(36.5+0j)
```

<br />
 
 
### **Exercise - 1** <a name="3.7"></a>

1. Tell the given **type** of the **variable** (single choice)

```python
name = "Mahesh"
b = type(name)
print(b)

A. int
B. <class 'int'>
C. <class 'str'>
D. string
```

2. which method is used to find the type of the variable for **a = 20** (single choice)

```python
A. print(a)
B. int(a)
C. str(a)
D. type(a)
```

3. Tell the correct **answers** from the following (multiple choice)

```python
A. a = "10"
B. b = "ram21"
C. c = 12
D. 1_d = 6
```

4. assign the **value** to the **variable** and print it.(short answer)

```python
 wonders_of_world =
 print()
```

5. write a **word** in the for the **variable** and print it (short answer)

```python
planet_near_to_sun=
print()
```

6. Write the **scientific notation** for given float number **0.002569** is (single choice)

```python
A. 2569e-5
B. 2.569e-3
C. 256.9e-4
D. 0.2569e-6
```

  <br />
  
  [go to Answers](#answers)

<br />

[go to List of Topics](#top)

  <br />

## **Variables** <a name="4"></a>

### **Python Variable** <a name="4.1"></a>

1. **Variable** is a name that is used to refer to a **memory location**.
2. Variables are also known as **identifiers** and they are used to hold specific values. Variable names can be a group of both the **letters** and **digits**, but they have to begin with a letter or an underscore.
   > we need not mention the datatypes of the variables because python automatically detects the types of the variables, based on the values that you assign to those variables.
3. Variables names are **case sensitive**. For example, there are two variables **amount** and another variable is **Amount**. Both the variables are different, and both of them will be accessed and used seperately.

```python
x = 10
_x = 20
```

Here the variable `x` and `_x` refers to an integer object. Leading Underscore before variable/function/method name indicates to programmer that It is for internal use only, that can be modified whenever class want.

The following are some examples of a few variables

```console
name = 'Ram'
Weight = 60
height = 80.50
```

We can get the data type of any object by using the `type()` function:
For Example :

```python
## Print the data type of the variable x:

>>> x = 5
>>> print(type(x))
<class 'int'>
```

Here the output provided by the interpreter is : `<class 'int'>` because an integer value is assigned to the variable `x`.

<br />
  
### **Common conventions followed for variable names** <a name="4.2"></a>
  
The following are the two most common types of variable naming conventions followed across the globe
  1. **Snake Case** : This looks like instead of space we use **underscore(_)**. For example is **name_of_the_student**
  2. **Camel Case** : This looks like for each new word it starts with **capital letter**. For example is **NameOfTheStudent**
  
<br />

> **PEP8** is Python's official style guide and it recommends : Function names should be lowercase, with words separated by underscores as necessary to improve readability. i.e., **Snake Case**

### **Creating good names** <a name="4.3"></a>

1. Variable names should be _meaningful_, _self explanatory_, and also they should **represent the purpose for which they are created**.
2. Meaningful variable names can make our **code more readable**, **easier to debug code** and also **maintain it**.
3. Some scenarios to explain why a proper naming convention is essential for **readability** of the code.
   - `n` - We cannot get any information from this variable name `n`.
   - `name` - able to understand but what name
   - `name_of_the_student` - very easy to understand and very appropriate for its purpose of usage.

<br />

### **Exercise - 2** <a name="4.4"></a>

1. Create a variable having the name: `student_name` and assign the value `Ramesh` to that newly created variable.
2. Given the problem to substract 5 from 10, using two variables with names: `number1` and `number2` and store the final result in `number3`.Print the final output.
3. Write a script that defines and uses the following variables for writing a meaningful english line

```console
colour = "blue"
fruit = "Mango"
number = 22
article = "is"
```

- use the variables above to print the following statements exactly

```console
sky is blue, Mango is yellow, age of suresh is 22 .
```

<br />

[go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **User input** <a name="5"></a>

1. They are **two** possibilities in which the user can give inputs to the python programs. They are :
1. Using `input()` function
1. Using **command line parameters (arguments)**.

### **input function** <a name="5.1"></a>

3. The `input()` function always takes the input given by user as a string by default. whatever input the user gives will automatically be converted to a string by the `input()` function.
4. The user should perform **type casting** to get back the actual type of the input that he provided to the program.

Examples for **input function**

```python
name_of_user = input("Name of the user: ")
print(type(name_of_user))
print(name_of_user)
print()

age_of_user = input("Age of the user: ")
print(type(age_of_user))
print(age_of_user)
print()

converted_age_of_user_to_integer = int(input("Age of the user: "))
print(type(converted_age_of_user_to_integer))
print(converted_age_of_user_to_integer)
```

```console
output

Name of the user: Ram
<class 'str'>
Ram

Age of the user: 15
<class 'str'>
15

Age of the user: 15
<class 'int'>
15
```

  <br />
  
 
### **Command line parameters (arguments)** <a name="5.2"></a>

1.  Command line parameters are also known as _Command line arguments_.
2.  The values or parameters that we would like to give as inputs within the program, are provided directly with the python script execution command, before we even run the program.
3.  A list of strings named `argv` is provided inside the code for values.
4.  Each value given in the command is consider as string and also have infinite number of values that are separated with spaces.
5.  To use `argv` we should import the module into the script

```python
 from sys import argv
```

6.  The variable `argv[n]` may be used to access each command line parameter in our program.

    - Here n is index of the value.
    - `argv[0]` is script name and `argv[1]`, `argv[2]`, etc are contains values.
    - Example
      PS C:\Users\Documents\Training\code> python test.py Ram 15 70.45

      1. test.py is `argv[0]`
      2. They are three command line parameters (arguments)

         - Ram is `argv[1]`
         - 15 is `argv[2]`
         - 70.45 is `argv[3]`

Examples for **command line parameters (arguments)**
Python script

```python
  from sys import argv
  num1 = argv[1]
  num2 = argv[2]
  num3 = int(argv[3])
  num4 = int(argv[4])
  addition1 = num1 + num2
  addition2 = num3 + num4
  print("The total addition1 result is", addition1)
  print("The total addition2 result is", addition2)
```

running script

> PS C:\Users\Documents\Training\code> python command_line_parameter.py 10 20 30 40

```console
# Output

The total addition1 is 1020
The total addition2 is 70
```

1. From the above script, the following are the few aspects to be remembered :
   - By default `argv`, consider any input argument that we provide as a string. So, we should explicitly type cast the value that are passed to the program via `argv`. We need to be clear of the data type that we will be type casting to within the program. So, the values that we send the program as input have to be apt their to actual datatypes (they should be easily type casted back to their respective types).

 <br />
    
 ### **Exercise - 3** <a name="5.3"></a>
 
 1. Write the script asking the user to give two integers and multiply them.
 2. Take the command line parameter any name you want (C:> C:\Users\Documents\Training\code> python command_line_parameter.py Girish and print in the following paragraph.
```python    
Girish is very good boy who helps everyone and also Girish participates in all the sports and cultural meet. Girish hobbies are playing virtual games and also watching movies.
```
 3. Write the script for calculating area of trainagle ( ask user to enter base and height).
 4. Write the script of the student form(name_of_student, class_studying, college_name, city_lives) that accepts as command line parameters and prints as
 ```python
  student_name : Hareesh sai
  class        : 12th
  college_name : SSB
  city_lives   : Hyderabad
 ```
* Here ```student_name``` value has spaces so keep in quotations to print the whole value. 
 
 <br />

[go to Answers](#answers)

 <br />
 
 [go to List of Topics](#top)

<br />

## **Operators** <a name="6"></a>

### **Numeric Operators** <a name="6.1"></a>

> +, -, \*, \*\*, /, //, %

Examples

```python
  # Addition
  >>> 4 + 7
  11
  # Subtraction
  >>> 8 - 3
  4
  # Multiplication
  >>> 3 * 5
  15
  # Exponent
  >>> 3 ** 3
  27
  # Floor division
  >>> 44 // 8
  5
  # Integer division
  >>> 44 / 8
  5.5
  # modulus divison
  >>> 44 % 8
  4
```

python script

```python
current = 5
resistance = 100
voltage = current * resistance
print("The given current is", current, "and resistance is", resistance, "So the total voltage flows in the circuit is", voltage, "V")
```

```console
# output

  The given current is 5 and resistance is 100 So the total voltage flows in the circuit is 500 V
```

  <br />

### **Assignment Operators** <a name="6.2"></a>

> +=, -=, \*=, \*\*=, /=, //=, %=

Examples

```python
x += y # is same as x = x + y
x -= y # is same as x = x - y
x *= y # is same as x = x * y
x **= y # is same as x = x ** y
x /= y # is same as x = x / y
x //= y # is same as x = x // y
x %= y # is same as x = x % y
```

```python
x = 2
y = 3
x += y
print(x)
x = x - y
print(x)
x = x * y
print(x)
x = x ** y
print(x)
x/= y
print(x)
x //= y
print(x)
x %= y
print(x)
```

```console
# output
5
2
6
216
72.0
24.0
0.0
```

 <br />

[go to List of Topics](#top)

<br />

### **Comparison Operators** <a name="6.3"></a>

> <, >=, <=, ==, !=, >

Examples

```python
  # greater than
  >>> 7 > 4
  True
  # less than
  >>> 7 < 4
  False
  # greater than or equla to
  >>> 7 >= 7
  True
  # less than
  >>> 7 <= 7
  True
  # equal to
  >>> 7 == 7
  True
  # not equal to
  >>> 7 != 7
  False
```

  <br />

### **Logical Operators** <a name="6.4"></a>

> and, or, not

1. `and` if the both the statements are `True` then we get final answer as `True`.
2. `or` if any one of the two statements is `True` then we get the final answer as `True`.
3. `not` it gives inverse of the final answer, when final answer is `False` then it gives `True`.

Examples

```python
 a = 10
 b = 5
 print( a > b and b == 5)
 print( b < a or b == 2)
 print(not( a > b ))
```

```console
# output

 True
 True
 False
```

 <br />
 
  
### **Membership Operators** <a name="6.5"></a>

> in, not in

1. `in` : if a value is **present** in the given list, `in` returns `True`.
2. `not in` : if a value is **not present** in the given list, `not in` returns `True`.

Examples

```python
names = ["Ramesh", "Suresh", "Ganesh"]
print("Ramesh" in names) # in operator
```

```console
# output

True
```

```python
names = ["Ramesh", "Suresh", "Ganesh"]
print("Hareesh" in names) # not in operator
```

```console
# output

True
```

 <br />
  
### **Identity Operators** <a name="6.6"></a>

> is, is not

1. `is` if the objects of both the variables to be same, `is` shows the result to be `True`.
2. `is not` if the objects of both the variables are different, `is not` shows the result to be `True`.

Examples

```python
a = ["Suresh", "Ganesh"]
c = a
b = ["Suresh", "Ganesh"]

print(a == b) # a is equal to b then returns True
print(a is c) # c is the same object as a it gives True
print(a is b) # a is not the same object as b, has a same values returns False
```

```console

# output

True
True
False

```

```python
a = ["Suresh", "Ganesh"]
c = a
b = ["Suresh", "Ganesh"]

print(a != b) # a is equal to b then returns False.
print(a is not c) # c is the same object as a it gives False.
print(a is not b) # a is not the same object as b, has a same values returns True.
```

```console

# output

False
False
True
```

<br />

### **Bitwise Operators** <a name="6.7"></a>

> &, |, ^, ~, <<, >>

1. ```&```  -   if both bits are 1 then set each bit to 1 (AND)
2. ```|```  -	if one of two bits is 1 then set each bit to 1 (OR)
3. ```^```  - 	if only one of two bits is 1 then Set each bit to 1 (XOR)
4. ```~```  - 	if the bit is 1 then it changes to 0 and also vice versa. (NOT)
5. ```<<``` - 	Move left by bringing in zeros from the right and letting the leftmost bits fall off (Zero fill left shift)
6. ```>>``` - 	Move right by copying the leftmost bit from the left and letting the rightmost bits fall off.(Signed right shift)
7. Examples
```python
a = 12
b = 6


print("Bitwise AND", a & b)
print("Bitwise OR", a | b)
print("Bitwise NOT", ~a)
print("Bitwise XOR", a ^ b)
```
```console
Bitwise AND 4
Bitwise OR 14
Bitwise NOT -13
Bitwise XOR 10
```

```python
right_shift = 10 #0000 1010 (Binary)
print(a >> 1)
left_shift = 5  #0000 0101 (Binary)
print(a << 1) 
```
```console
#output
5
10
```

<br />

[go to List of Topics](#top)

<br />

### **Exercise - 4** <a name="6.8"></a>

1.  Tell the answer for given Expression without running it using python interpreter

```python
print(20 / 2)
```

```console
A. 10.0
B. 10
C. 10.00
```

2.  Go through the code without running it using python interpreter

```python
a = 5
b = 10
if a ** 2 > 50 and b < 50:
   print(a, b)
```

```console
A. 5 10
B. No Answer
C. 25 10
```

3. See the expression and give answer without running it using python interpreter

```python
number = (45 - 3 ** 3) / 6
print(number)
```

```console
A. 4.0
B. 3.0
C. 18.0
```

4. Go through the code and give the all the values without running it using python interpreter

```python
a = 2
b = 10
c = 6
a += b
b %=c
print(a, b)
print(c > b)
print(a == (a + b + c) - 20)
d = a < c or a != 12
print(d)
```

5. Go through the code without running it using python interpreter

```python
x = "kumari"
y = "ma"
print(y not in x)
```

<br />

[go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **Strings** <a name="7"></a>

1. Strings can be enclosed in **single quotes** or **double quotes**.

> Example :- "Multiple_wishes" 'Multiple_wishes'

2. In the case of string handling, the operator `+` is used to concatenate two strings as the operation ```"Multiple"```+```" Wishes"``` returns ```"Multiple Wishes"```.

<br />

### **Indexing** <a name="7.1"></a>

1. To retrieve an element of the list, we use the **index** operator `[ ]` :

&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5&nbsp;&nbsp;&nbsp;&nbsp; 6&nbsp;&nbsp;&nbsp;&nbsp; 7&nbsp;&nbsp;&nbsp;&nbsp; - Indexing

&nbsp;&nbsp;↓ &nbsp;&nbsp;&nbsp;&nbsp; ↓&nbsp; &nbsp;&nbsp;&nbsp; ↓&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; ↓&nbsp;&nbsp;&nbsp;&nbsp; ↓&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓&nbsp;&nbsp;&nbsp;&nbsp; ↓&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓

'M',&nbsp;&nbsp; 'U', &nbsp;&nbsp;'L',&nbsp;&nbsp;&nbsp; 'T', &nbsp;&nbsp;'I', &nbsp;&nbsp;'P', &nbsp;&nbsp;'L', &nbsp;&nbsp;&nbsp;'E',

&nbsp;&nbsp;↑ &nbsp;&nbsp;&nbsp;&nbsp; ↑&nbsp; &nbsp;&nbsp;&nbsp; ↑&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; ↑&nbsp;&nbsp;&nbsp;&nbsp; ↑&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↑&nbsp;&nbsp;&nbsp;&nbsp; ↑&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↑&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;-8&nbsp;&nbsp;&nbsp;&nbsp; -7&nbsp;&nbsp;&nbsp; -6&nbsp;&nbsp;&nbsp; -5&nbsp;&nbsp;&nbsp; -4&nbsp;&nbsp;&nbsp; -3&nbsp;&nbsp;&nbsp; -2&nbsp;&nbsp;&nbsp; -1&nbsp;&nbsp;&nbsp; -Reverse indexing

Example :-

```python
name = "multiple"
print(name[3])
```

```console

#Output:
t
```

<br />

[go to List of Topics](#top)

<br />

### **Object Identity** <a name="7.2"></a>

1. In Python, every created **object** identifies **uniquely** in Python.
2. Python provides the guaranteed that **no two objects will have the same identifier**. The built-in ```id()``` function, is used to identify the object identifier.
> The following program illustrates the assignment and reassignment of values to objects.

```python
a = 50
b = a
print("Id of a variable is",id(a))
print("Id of b variable is",id(b))
# Reassigned variable a
a = 500
print("Id of a variable is",id(a))
```

```console
Output:
Id of a variable is 140734982691168
Id of b variable is 140734982691168
Id of a variable is 2822056960944
```

<br />

### **Program using builtin function**: <a name="7.3"></a>

1. The following examples demonstrate the usage and importance of  *accessing*, *updating*, *formating*, *slicing*, *concatenating* and *escaping* in strings

> Example - 1

```python
str1 = "Multiple_Wishes"
str2 = "Py_wishes"
print("Id number for str1 is ", id(str1), "\n" "Id number for str2 is ", id(str2))
# str1[1] = 'a' # illegal, since strings are (immmutable)
# new string created from old ones
str1 = str1[:1] + 'i' + str1[6:]
print("by indexing and adding i str1 is :", str1, str2)
print("Now str1,str2 id's are: ", id(str1), id(str2))
Name = "Multiple_Wishes"
print("Finding the letter index ", Name.index('e'))
print(Name.index('is'))
print('a' in Name)
print(Name.upper(), Name.lower())
print(Name.replace('p', 'b'))
Symbol = ";"
print(Symbol.join(('Multiple_Wishes', 'Hyd', 'India')))
Name = "Multiple_Wishes"
print("Printing name 3times: ", Name*3, "\n" "Length of name is: ",len(Name))
print(Name[0:10])
Str_name = "hello123"
print("Is Str_name contains numbers: ", Str_name.isalnum(), "\n" "Is string name contains Alphabets: ", Str_name.isalpha())
val = "123"
print(val.isdigit())
Name = "Multiple_Wishes"
print(Name.isalpha())
```
```console
#Output:
Id number for str1 is  1608101425520
Id number for str2 is  1608101425264
by indexing and adding i str1 is : Mile_Wishes Py_wishes
Now str1,str2 id's are:  1608106224688 1608101425264
Finding the letter index  7
10
False
MULTIPLE_WISHES multiple_wishes
Multible_Wishes
Multiple_Wishes;Hyd;India
Printing name 3times:  Multiple_WishesMultiple_WishesMultiple_Wishes
Length of name is:  15
Multiple_W
Is Str_name contains numbers:  True
Is string name contains Alphabets:  False
True
False
```
The function ```eval()``` evaluates the passed string as a Python expression and returns the result. For example, ```eval("1 + 2")``` interprets and executes the expression ```"1 + 2"``` and returns the result (3).

> Example - 2

```python
# Using Backslash to continue statements
a = 2 + \
1.5 * 3
print("a = ", a)
b = eval("5.2") + 3
print("b = ", b)
print(eval("4 < 10"))
print(eval("'Multiple_wishes '  * 5"))
print(eval("abs(-11)"))
print(eval('"Multiple_Wishes".upper()'))
# print(eval('os.getcwd()'))
c = eval("2.3") + 2
print("c = ", c, type(c))
d = "3.2" + "3"
print("d = ", d, type(d))
# use the implicit continuation inside parenthesis
e = ([5, 12, 13, 200])
print("e1 = ", e)
```

```console

#Output:
a =  6.5
b =  8.2
True
Multiple_wishes Multiple_wishes Multiple_wishes Multiple_wishes Multiple_wishes
11
MULTIPLE_WISHES
c =  4.3 <class 'float'>
d =  3.23 <class 'str'>
e1 =  [5, 12, 13, 200]
```

<br />
  
[go to List of Topics](#top)

<br />

### **Formatting with `.format method`** <a name="7.4"></a>

1. Example:

```python
string_name = "multiple_wishes"
print(f"Name of the string is : {string_name}")
#or
print("Name of the string is : {}".format(string_name))
```

```console
#Output :
Name of the string is : multiple_wishes
Name of the string is : multiple_wishes
```

Here by using ```.format``` the ```string_name``` is inserted in `{}`.

<br />
  
## **Important points to remember** <a name="7.5"></a>

1. Python includes methods for converting any value to a string, such as `repr()` and `str()`.
2. The `str()` method is intended to yield **human-readable** representations of values, whereas `repr()` is intended to provide **interpreter-readable** representations . When providing output for end users, almost always use str.
3. The `repr()` function is mostly for **troubleshooting and exploration**. For example, if you think a string has non-printing characters or a float contains a little rounding mistake, `repr()` will disclose it but `str()` may not.

```python
s="genesis"
"""
   The string 'genesis' has the name s connected to it. When you call str(s),
   the interpreter replaces s with 'genesis' and then calls str('genesis').
"""
print(str(s))
print(repr(s))
```

```console
# output

genesis
'genesis'
```

<br />

### **Python has builtin functions, methods & keywords for string. They are used for program:** <a name="7.6"></a>

- [Python Built in Functions](https://github.com/saikrishnavadali05/python3_ebook/blob/36c9f6d569020420975b78432e6f093a21c3829c/Methods&keywords/PYTHON_BUILTIN_FUNCTION.MD)
- [Python String Methods](https://github.com/saikrishnavadali05/python3_ebook/blob/36c9f6d569020420975b78432e6f093a21c3829c/Methods&keywords/STRING_BUILTIN_METHODS.md)
- [Python keywords](https://github.com/saikrishnavadali05/python3_ebook/blob/36c9f6d569020420975b78432e6f093a21c3829c/Methods&keywords/Python%20Keywords.MD)


<br />

## **Slicing Operator** in Lists and Strings <a name="7.7"></a>

The syntax is:
```python
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
```
There is also the step value, which can be used with any of the above:
```python
a[start:stop:step] # start through not past stop, by step
```
The key point to remember is that the ```:stop``` value represents the first value that is not in the selected slice. So, the difference between stop and start is the number of elements selected (if step is 1, the default).

The other feature is that start or stop may be a negative number, which means it counts from the end of the array instead of the beginning. So:

```python
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
```
Similarly, step may be a negative number:
```python
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```
Python is kind to the programmer if there are fewer items than you ask for. For example, if you ask for ```a[:-2]``` and a only contains one element, you get an empty list instead of an error. Sometimes you would prefer the error, so you have to be aware that this may happen.

Relationship with the slice object
A slice object can represent a slicing operation, i.e.:

```a[start:stop:step]```
is equivalent to:
```a[slice(start, stop, step)]```
Slice objects also behave slightly differently depending on the number of arguments, similarly to ```range()```, i.e. both slice(stop) and slice(start, stop[, step]) are supported. To skip specifying a given argument, one might use None, so that e.g. a[start:] is equivalent to a[slice(start, None)] or a[::-1] is equivalent to a[slice(None, None, -1)].

While the `:`-based notation is very helpful for simple slicing, the explicit use of slice() objects simplifies the programmatic generation of slicing.

  
### **Exercise - 5** <a name="7.8"></a>

1.  Write a script that can convert the given lower string to upper case string

```console
For Example :
Input string : python 
Output string : PYTHON
```

2.  Write a script that can replace the first character in string

```console
For Example :
Input string : Cython
Output string : Python
```

3.  Write a script that prints the following output (use ```center()``` method)

```console
# output

****Python****
```

4.  Please go through the code and provide the answer without running the code in any interpreter

```python
string = "Hello, emma."
result = string.index("e")
print(result)
```

<br />

[go to Answers](#answers)
<br />

[go to List of Topics](#top)

<br />



## **Escape sequences** <a name="8"></a>

1.  The character `\` represents the beginning of an escape sequence.
2.  Table of escape sequence

| Sequences |  represents  |
| :-------- | :----------: |
| \b        |  backspace   |
| \n        |   newline    |
| \t        |     tab      |
| \r        |    return    |
| \a        |     bell     |
| \\\       |  backslash   |
| \\"       | double quote |
| \\'       | single quote |

3. examples of escape sequences statements

```python
>>> print("He's \"very good\" boy.\n")
He's "very good" boy.

>>> print("He's \"very good\" boy.")
He's "very good" boy.
>>> print("He\tis\tvery\tgood\tboy.")
He      is      very    good    boy.
```

<br />

### **Exercise - 6** <a name="8.1"></a>

1. Write a script to print the following statements using escape sequences and output should look like the following

```console
# output
Talk is 'cheap'. Show me the code.
I'm not a "great" programmer!I'm just a  good programmer with great habits.
If your ship doesn 't come in, \swim\ out to it?
```

2. write a script to display the following shape using ```print()``` statements

```console
         *
     * python *
   * is  *  a    *
 * good  * programming * language *
* to * learn * for * beginners *
```

 <br />

[go to Answers](#answers)

  <br />
  
  [go to List of Topics](#top)
  
  <br />
   
## **Conditional statements** <a name="9"></a>

### ```if``` statement: <a name="9.1"></a>

1. ```if``` statement is the most simple ***decision-making*** statement.
2. It is used to decide whether a certain statement or block of statements will be executed or not based on certain conditions that we provide after the ```if``` keyword i.e, if a certain condition is satisified or ```True```, then the block of statements under if will be executed. if that condition is not satisfied or ```False```, the statements that are under the ```if``` block are not executed. 
3.  For an ```if``` statememt, the ```elif``` and ```else``` blocks are **optional**. 
4.  while writing ```if``` statements, we should make sure that, we are writing the code with **proper indentation**, otherwise the code execution stops, displaying indentation related errors. 

5. Some of the condition checks than can be done within an `if` statement:

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

> Example for a simple `if` statement:

```python
weight = int(input("give your weight "))
if(weight > 70):
  print("You have to reduce your weight.")
```

```console
 Script Execution in Command Prompt
  PS C:\Users\Documents\Training\code> python conditions.py

 Output :
 give your weight 80
 You have to reduce your weight.
```

> Example for an `if` - `else` statement:

```python
number = int(input("Enter the number "))
if number > 40:
    print("you are old")
else:
    print("you are young")
```

```console
Script Execution in Command Prompt
PS C:\Users\Documents\Training\code> python conditions_1.py

output
Enter the number 12
you are young
```

> Example for an `if`-`elif`-`else` statement:

```python
Mutiple_wishes = int(input("Please enter an integer: "))
if Mutiple_wishes < 0:
    print('Less than zero')
elif Mutiple_wishes == 0:
    print('Zero')
else:
    print('greater than zero')
```

```console
Output:
Please enter an integer: 1
greater than zero
```

 <br /> 
  
### **Exercise - 7**  <a name="9.2"></a>
  
  1. Write a script to check whether the given year is a *leap year* or not. The input i.e., year, should be given during script execution itself. i.e, as a command line parameter.
  2. Write a script to check whether the given number is *odd or even* by requesting input from the user, using ```input()``` function.
  3. Write a script that requests the user to give an input which is a random value in *inches* and the script shall convert the *inches* value to *feets and inches*
  
  ```console
  For Example,
    If the input from the user is : 27 
    The program shall consider the input to be 27 inches.
    The output that the program shall provide is 2 feet 3 inches.
  ```
 
  
   <br /> 
  
  [go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **Loops**<a name="10"></a>

### **``While loop```** <a name="10.1"></a>

1. syntax for `while` is

```console
  While expression:
    code to write
```

    - the code in the while executes continously as long as the expression evaluates to be true.
    - When the expression evaluates as False, then the loop terminates.

2. Examples of `while` loop
```python
i = 2
while i > 0:
  print(" i is ", i)
  i = i - 1
print("loop executed")
```

```console
running script
PS C:\Users\Documents\Training\code> python while_statement.py

output
i is  2
i is  1
loop executed
```

### **```for```** loop <a name="10.2"></a>

1. The ```for``` loop in Python is used to **iterate the statements** or a part of the program several times. 
2.  It is frequently used to traverse the data structures like list, tuple, or dictionary.

3.   Example:


```python
str = "MultipleWishes"
for i in str:
    print(i)

Output:
M
u
l
t
i
p
l
e
W
i
s
h
e
s
```

4.  Example of `for` loop using `f` formatting:

```python
s = "Multiple_wishes"
"""
Name s is attached to 'Multiple_wishes' string. When you call str(s) the
interpreter puts 'Multiple_wishes' instead of s and then calls str('Multiple_wishes').
"""
print(str(s))
print(repr(s))
for x in range(1, 7):
    print(str(x).rjust(2), str(x*x).rjust(5), sep=":", end=" ")
    # Note use of 'end' in the above
    print(str(x*x*x).rjust(4), end=" ")
    print(str(x*x*x*x).rjust(4), end=" ")
    print(str(x*x).rjust(6))

print()
for x in range(1, 5):
    print('{0:2d} {1:4d} {2:4d}'.format(x, x*x, x*x*x))
print()
print('12'.zfill(10))
print('3.14159265'.zfill(5))
print('-3.14'.zfill(6))
print('{0:2} {1:2} {2:2}'.format('company', 'and', 'Multiple_wishes'))
print()
print("PI value is approximately {0:.5f}".format(3.14159265))
print('{0} is {1}'.format('Country', 'India'))
print('{1} {2} {0}'.format('Country', 'India', 'is'))
print('Our {key} is {data}'.format(key='country', data='india'))
print('{0} {company}'.format('Multiple_wishes', company='dream'))
```

```console
Outputs

Multiple_wishes
'Multiple_wishes'
 1:    1    1    1      1
 2:    4    8   16      4
 3:    9   27   81      9
 4:   16   64  256     16
 5:   25  125  625     25
 6:   36  216 1296     36

 1    1    1
 2    4    8
 3    9   27
 4   16   64

0000000012
3.14159265
-03.14
company and Multiple_wishes

PI value is approximately 3.14159
Country is India
India is Country
Our country is india
Multiple_wishes dream
```

### **```for``` loop help in lists**

```python
My_Lists = ['Multiple_Wishes', 'Pywishes', 'Hyderabad']
for x in My_Lists:
    print("length of", x, "is", len(x))

name = []

for x in My_Lists:
    if len(x) > 8: name.insert(0, x)
print(name)

months = ['jan', 'feb', 'march', 'april']
for i in range(4):
    print(f"month {i+1}:", (months[i]))

months = ['july', 'august', 'september', 'october']
for num, name in enumerate(months, start=7):
    print(f"month {num}: {name}")
```

```console
Output:
length of Multiple_Wishes is 15
length of Pywishes is 8
length of Hyderabad is 9
['Hyderabad', 'Multiple_Wishes']
month 1: jan
month 2: feb
month 3: march
month 4: april
month 7: july
month 8: august
month 9: september
month 10: october
```

 <br />

### **Exercise - 8** <a name="10.3"></a>

1.  Write a script that takes a `list` and find the largest number and smallest number using `while` and `for` loops.

```console
 	input list = [7, 3, 9, -23, 0, -21, 2]
	The output should show that the
	largest number is 9 and the smallest number is -23
```

2.  Write a script for factorial and take input from the command line parameter. using `while` and `for` loops

```console
For example, factorial of 4! is 4 * 3 * 2 * 1 = 24.
Input of your code should take n as input.
Output of your code should be n!
```

3.  Write a script to print the count of number of digits within the given input number using `while` and `for` loops. 

```console
input from the user is 123.
number of digits in the above number are 3.
Hence the output count should return 3.
```

<br />
  
[go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **Lists** <a name="11"></a>

1. A ```list``` in Python is used to store the **sequence of various types of data**. 
2. Python lists are **ordered** and **mutable** type its mean we can modify its element after it created. 
3. The items in the list are separated with the (comma) ```,``` and enclosed with the square brackets ```[]```. Lists can contain items of different types.

Basic examples

```python
>>> numbers = [0, 5, 8, 11, 12]
>>> months = ["january", "March", "April"]
>>> student = ["suresh", 80, 6.2] #list also contain different data types
```

<br />

[go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **```range``` function:** <a name="12"></a>

1. If you do need to iterate over a **sequence of numbers**, use the built-in function ```range()```. 
2. It generates lists containing arithmetic progressions:

 - Python’s `range(1, 10)` function returns a list of consecutive integers, in this case the list ```[1,2,3,4,5,6,7,8,9]```.
   So, the `for` statement `for i in range(1, 10))` is equivalent to:

```python
for i in [1,2,3,4,5,6,7,8,9]
```

> An example scenario containing the usage of `range()` function:

```python
for i in range(1, 5):
    print(i, " ", i * i)
print()
for i in range(0, 25, 5):
    print(i, " ", i * i)
print()
print(list(range(0, -10, -2)))
```

```console
Output:

1   1
2   4
3   9
4   16

0   0
5   25
10   100
15   225
20   400

[0, -2, -4, -6, -8]
```

It is possible to nest a lists (create lists containing other lists) within another list.

> An example code snippet to illustrate nested lists:

```python
data = ["a", 'b', 10, 3]
print(data)
print(data[1], data[1:-1])
print(data[:2], ['c', 3 * 1])
data[2:3] = [20, 30]  # change items
print(data)
data[2:4] = []  # remove items
print(data)
data[2:2] = [15, 18, 22]  # insert items
print(data)
print("length of data", len(data))
# nesting of lists
a = [10, 20, 12, 3]
b = [5, a, 30]
print(b)
print(b, b[1])
a.sort()
print(a)
b[1].append(25)
print(b)
```

```console
Output:

['a', 'b', 10, 3]
b ['b', 10]
['a', 'b'] ['c', 3]
['a', 'b', 20, 30, 3]
['a', 'b', 3]
['a', 'b', 15, 18, 22, 3]
length of data 6
[5, [10, 20, 12, 3], 30]
[5, [10, 20, 12, 3], 30] [10, 20, 12, 3]
[3, 10, 12, 20]
[5, [3, 10, 12, 20, 25], 30]
```

> An example code snippet of a list being used along with **membership** operators

<br />

```python
>>> student = ["Ramesh", 80, 6.65]
>>> "Ramesh" in stuff
True
>>> 80 not in stuff
False
```

<br />
   
 
### **Exercise - 9** <a name="12.1"></a>
  
 1. write output for the given questions
 ```console
 1. [0, 2, 4, 6]
 2. [20, 16, 12, 8, 4]
 3. [-12, -6, 0, 6, 12]
 4. range(2, 5)
 5. range(12, -3, -3)
 6. range(10, 30, 10)
 ```

  <br />  
  
  [go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **Tuples:** <a name="13"></a>

1. Tuples are like lists, but are **ordered** and **immutable** like strings, i.e. unchangeable (it is not possible to assign to the individual items of a tuple).
2. They are enclosed by **parentheses** or nothing at all, rather than brackets.

```python
t1 = (12, 5, 8)
print("index 1 in t1 is :", t1[1])
print(len(t1), max(t1), min(t1))
# t1[0] = 10 # illegal, due to immutability
t2 = ("hello", 5)
t3 = (t1 + t2)
print(t3)
print(5 in t1)
for val in t1:
    print(val)
print(t1[1:])
del t1
print(t3)
# print(t1) throws error as we deleted t1
print(type(t2[0]))
print(type(t3))
```
```console
Output:

index 1 in t1 is : 5
3 12 5
(12, 5, 8, 'hello', 5)
True
12
5
8
(5, 8)
(12, 5, 8, 'hello', 5)
<class 'str'>
<class 'tuple'>
```

If we want to change or add values to the tuple then we can only achieve it by changing the ```tuple``` into ```list```, then update(add/remove) items to it and convert back to tuple.

```python
phone_tuple = ("Redmi", "LG", "Apple")
phone_list = list(phone_tuple)
phone_list.append("Realme")
phone_tuple = tuple(phone_list)
print(phone_tuple)
```
```console
running script
PS C:\Users\Documents\Training\code> python lists.py

output
('Redmi', 'LG', 'Apple', 'Realme')
```

 <br />
  
 
### **Exercise - 10** <a name="13.1"></a>
  
 1. Write a python script that does the following operations:
 ```console
 Input to the script will be a tuple with bike names : ("pulsar", "duke", "shine")

 *Script should* : 
 1. give the total number of items present in the tuple.
 2. give the index number for "shine" in the tuple.
 3. add the item "splendor" to the tuple.
 4. remove the item "duke" from the tuple.
 ```
  
<br />
  
  [go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **Sets** <a name="14"></a>

1. A ```set``` contains uniques values in it. It is denoted with *curly braces :* `{}`. The values in the ```set``` are unordered and also it deletes the duplicate values. Once the ```set``` is created, we can not update the existing values. But new values can be added (appended). In ```set``` we cannot access values with the help of index, which is possible in tuples and lists easily.
2. A few examples of code snippets showing the usage of sets

```python
name_set = {"Harish", "Ramesh", "Suresh"}
for i in name_set:
print(i)
```

```console
running script
PS C:\Users\Documents\Training\code> python set.py

output
Harish
Ramesh
Suresh
```

> A Few examples of methods in a ```set```  

```python
name_set = {"Harish", "Ramesh", "Suresh"}
name_set.add("Mahesh")
name_set.remove("Harish")
print(name_set)
```

```console
running script
PS C:\Users\Documents\Training\code> python set_1.py

output
{'Ramesh', 'Suresh', 'Mahesh'}
```

<br />

### **Exercise - 11**<a name="14.1"></a>

1. Write a python script that takes the following two sets as inputs and does the following operations on those sets :

```python
# Input Sets :
set1 = {"maaza", "sprite", "fanta", "maaza"}
set2 = {"pepsi", "frooti", "sprite", "maaza"}
```

```console
 Operations to be done on those Sets :
 1. Remove the duplicate elements from the set1.
 2. Add an item "7_up" to the set1.
 3. Duplicate the elements of set1 to a new backup set.
 4. Compute the union and intersetion of set1 and set2.
 5. Compute the difference of set1 from set2.
 6. Then remove the "pepsi" element from the set2.
 7. Then remove all elements from set1
```

<br />
  
  [go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **Dictionary:** <a name="15"></a>

1. Dictionary (hash) which is also called **associative arrays**. 
2. Dictionary is a built-in Python Data Structure that is **mutable**. 
3. Dictionaries are used to store data values in **key:value** pairs. 
4. A dictionary is a collection which is **ordered**. 
5. Deletion of an element from a dictionary can be done via ```pop()```. The ```in``` operator works on dictionary keys. 
6. As of Python **version 3.7**, dictionaries are **ordered**. In Python **3.6** and earlier, dictionaries are **unordered**.

> An example program to illustrate the creation and usage of a dictionary

```python
  user_dict = {
  "name": "Ganesh",
  "Age": 18,
  "Weight": 60,
  "Height": 5.8
}
student = thisdict["name"]
print(student)
```
```console
Script Execution and Outputs
PS C:\Users\Documents\Training\code> python dictonary.py

Output : 
Ganesh
```

> Another example program to illustrate a dictionary:

```python
months = {4: 'April', 2: 'Feb', 5: 'May', 1: 'Jan'}
print(months)
print(months[4])
months[3] = 'March'
print(months)
print("keys assigned in dictionary :", months.keys())
print("values assigned to keys :", months.values())
del months[2]
for key in months:
    print(key, months[key])
print(months.pop(3))
print(months)
print(5 in months)
print(3 in months)
print(months.get(1))
# del months
months.clear()
print(months)
```
```console
# Output

{4: 'April', 2: 'Feb', 5: 'May', 1: 'Jan'}
April
{4: 'April', 2: 'Feb', 5: 'May', 1: 'Jan', 3: 'March'}
keys assigned in dictionary : dict_keys([4, 2, 5, 1, 3])
values assigned to keys : dict_values(['April', 'Feb', 'May', 'Jan', 'March'])
4 April
5 May
1 Jan
3 March
March
{4: 'April', 5: 'May', 1: 'Jan'}
True
False
Jan
{}
```

> Another example program to illustrate the usage and purpose of a dictionary in python

```python
Dict_my = {}
# Creating a Dictionary with Mixed keys
Dict_my = {'Name': 'Multiple_wishes', 1: [1, 2]}
Dict_my[1] = 5, 6
Dict_my[2] = 2, 3, 4
print("\nDictionary with the use of Mixed Keys: ")
Dict_my[3] = {'Nested': {1: 'Hyderabad', 2: 'Telangana'}}
print(Dict_my)
print(Dict_my[3]['Nested'][2])
# Creating a Dictionary with dict() method
Dict_my = dict({1: 'Multiple_wishes', 2: 'Py_wishes', 3: 'Company'})
print("\nDictionary with the use of dict(): ")
print(Dict_my)
# Creating a Dictionary with each item as a Pair
Dict_my = dict([(1, 'Multiple_wishes'), (2, 'Hyderabad')])
print("\nDictionary with each item as a pair: ")
print(Dict_my)
cubes = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
for i in cubes:
    print(cubes[i])
print("Len = ", len(cubes))
print("\nby using range statement")
for i in range(1, 6):
    print(i ** 3)
```
```console
Output:

Dictionary with the use of Mixed Keys:
{'Name': 'Multiple_wishes', 1: (5, 6), 2: (2, 3, 4), 3: {'Nested': {1: 'Hyderabad', 2: 'Telangana'}}}
Telangana

Dictionary with the use of dict():
{1: 'Multiple_wishes', 2: 'Py_wishes', 3: 'Company'}

Dictionary with each item as a pair:
{1: 'Multiple_wishes', 2: 'Hyderabad'}
1
8
27
64
125
Len =  5

by using range statement
1
8
27
64
125
```

<br />

[go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **OrderedDict module** <a name="15.1"></a>

An ```OrderedDict``` is a dictionary subclass that remembers the order in which its contents are added, supporting the usual ```dict``` methods. If a new entry overwrites an existing entry, the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.

> Example : OrderDictionary1.py

```python
from collections import OrderedDict
od = OrderedDict()
od['c'] = 1
od['b'] = 2
od['a'] = 3
print(od.items())
d = {}
d['c'] = 1
d['b'] = 2
d['a'] = 3
print(d.items())

Output:

odict_items([('c', 1), ('b', 2), ('a', 3)])
dict_items([('c', 1), ('b', 2), ('a', 3)])
```

> Example : OrderDictionary2.py

Key value Change: Even if the value of a certain key is changed, the position of the key remains unchanged in an ```OrderedDict```.

```python
from collections import OrderedDict
print("Before:")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
print("\nAfter:")
od['c'] = 5
for key, value in od.items():
    print(key, value)

Output:

Before:
a 1
b 2
c 3
d 4

After:
a 1
b 2
c 5
d 4
```

> Example : OrderDictionary3.py

**Deletion and Re-Insertion** - Deleting and re-inserting the same key will push it to the back as ```OrderedDict```, however, maintains the order of insertion.

```python
from collections import OrderedDict
print("Before deleting:")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
print("\nAfter deleting:")
od.pop('c')
for key, value in od.items():
    print(key, value)
print("\nAfter re-inserting:")
od['c'] = 3
for key, value in od.items():
    print(key, value)

Output:

Before deleting:
a 1
b 2
c 3
d 4

After deleting:
a 1
b 2
d 4

After re-inserting:
a 1
b 2
d 4
c 3
```

> Example : OrderDictionary4.py

```python
import collections
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d2 = {}
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'
print('dict:', d1 == d2)
d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d2 = collections.OrderedDict()
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'
print('OrderedDict:', d1 == d2)

Output:

dict: True
OrderedDict: False
```

> Example : OrderDictionary5.py

```python
import collections
d = collections.OrderedDict(
[('a', 'A'), ('b', 'B'), ('c', 'C')]
)
print('Before:')
for k, v in d.items():
    print(k, v)
d.move_to_end('b')
print('\nmove_to_end():')
for k, v in d.items():
    print(k, v)
d.move_to_end('b', last=False)
print('\nmove_to_end(last=False):')
for k, v in d.items():
    print(k, v)
```

```console
Output:

Before:
a A
b B
c C

move_to_end():
a A
c C
b B

move_to_end(last=False):
b B
a A
c C
```

The only difference between ```dict()``` and ```OrderedDict()``` is that: ```OrderedDict``` preserves the order in which the keys are inserted.

<br />
 
 
### **Exercise - 12** <a name="15.2"></a>
  1. Write a python script that contains a dictionary with name : "details" and the script should perform the steps from 1 to 7.
 ```console
 
 Consider the following Dictionary  :
  
  details = {
              "name": "Steve",
              "education": "Reed College",
              "born": 1955
            }

 1. Print all the keys and values from the dictionary separately.
 2. Add a new key "died" and assign the value "2011" to the above dictionary. And then print the updated dictionary again.
 3. Remove the "education" key from the dictionary and print the changed dictionary again.
 4. Create another duplicate dictionary with name "details_duplicate" from the above dictionary to have a backup of the existing dictionary.
 5. Retrieve the values of the dictionary just by using corresponding keys.
 6. Remove all the elements of the "details" dictionary and then print the entire empty dictionary.
 7. Print the entire duplicate dictionary
```
   
 <br />
  
[go to Answers](#answers)



[go to List of Topics](#top)

<br />
	
### Python Functions <a name="16"></a>
1. Functions are the most important aspect of an application. 
2. A function can be defined as the organized block of **reusable code**, which can be called whenever required. 
3. The keyword ```def``` introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters.
4. The Function helps to programmer to break the program into the smaller part. It **organizes** the code very effectively and **avoids** the repetition of the code. As the program grows, function makes the program more organized.
5. There are mainly two types of functions.

- User-define functions - The user-defined functions are those define by the **user to perform the specific task**.

- Built-in functions - The built-in functions are those functions that are **pre-defined** in Python.

6.Example of Function 1:
```python
def square(a):
 return a * a

print(square.__doc__)

val = square(3)
print(val)
print(type(val))

val = square
print("val(2)",val(2))
```
```console
Output:
None
9
<class 'int'>
val(2) 4
```  
 
7. Example of Functions 2: 
 ```python
def sumodd(n = 5):
  val = 0
  index = 1
  while (index <= n):
  # if even we continue with next iteration
    if (index % 2 == 0):
      index += 1
      continue
  # if odd we add it
    val += index
    index += 1
  return val
def funNotImplemented(): pass
print("sumodd is", sumodd(3))
print("sumodd is", sumodd())
funNotImplemented()
```
```console
Output:
sumodd is 4
sumodd is 9
```  
8.Example of Functions 3 with Keyword Argument:
```python
def funckeyword(arg1, arg2='Multiple', arg3='Wishes'):
  print("arg1=", arg1, "arg2=", arg2, "arg3=", arg3)
funckeyword(10)
funckeyword(arg1="value1")
  
funckeyword(10, arg2="Multiple")
funckeyword(10, arg3="Wishes", arg2="MultipleWishes")
funckeyword(arg3="Hyderabad", arg1="value1")
```
```console
arg1= 10 arg2= Multiple arg3= Wishes
arg1= value1 arg2= Multiple arg3= Wishes
arg1= 10 arg2= Multiple arg3= Wishes
arg1= 10 arg2= MultipleWishes arg3= Wishes
arg1= value1 arg2= Multiple arg3= Hyderabad
```

 <br />
   
 ## **Exercise-12** <a name="16.1"></a>
  
 1. Write a function that take string as a parameter. the string is given by the user as input. the final output from the function is to reverse the string.
 ```python
  example the string is Multiple - output is elpitluM
 ```
 2. Write a function that print the reverse of the given number. The input is given in the command line parameter.
 ```python
  example the number is 456 - output os 654.
 ```
 3.  Write a function that take three integers and compare which the largest and smallest among the them. take input from the end user.
 ```python
  example the given numbers are 45, 22, 60 - output is largest is 60 and smallest is 22
 ```
 [go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />

## **Python Modules** <a name="17"></a>

1. Python relies heavily on modules. A Python module is a file that contains Python definitions and statements. The file name is the module name plus the suffix '.py'.
2. Module definitions can be imported into other modules or the main module.
3. Example
 - Let us employ the addition module (addition.py). Enter the Python interpreter and run the following command to import this module.
 PS C:\Users\Documents\Training\code>python
 ```python
 >>> import addition
 ```
 - This just adds the module name  addition to the existing symbol table, not the names of the functions added in addition. The functions can be accessed by using the module name, as illustrated below.
 ```python
 >>> addition.add(5,6)
 ```
 - If you intend to use a function frequently, you may give it a local name:
 ```python
 >>> add_func = addition.add(4,5)
 >>> add_func
 ```
4. A module have both executable statements and function definitions. These statements are used to get the module started. They are only executed the first time the module is imported. 
5. example:
```python
>>> from addition import add, add_to_n
>>> add(7, 8)
>>> add_to_n(3)
```
6. example
```python
>>> from fibonacci import *
All names except those beginning with an underscore (_) are imported.
```
7. When you import a module called addition, the interpreter looks for a file called 'addition.py' in the current directory, then in the list of directories given by the environment variable PYTHONPATH.
8. When the Python interpreter is run with the -O switch, optimised code is created and saved in.pyo files. The optimizer is currently ineffective; it simply eliminates assert statements. When -O is used, all bytecode is optimized;.pyc files are ignored, while.py files are compiled to optimised bytecode.
9. Passing two -O options to the Python interpreter (-OO) causes the bytecode compiler to execute optimizations, which may result in malfunctioning applications in rare instances. Only __doc__ strings are currently deleted from the bytecode, resulting in smaller '.pyo' files. Because certain programmes may rely on having them available, you should exercise caution while using this option.
10. A programme does not execute any quicker when read from a '.pyc' or '.pyo' file than when read from a '.py' file; the only difference is the speed with which '.pyc' or '.pyo' files are loaded.
11. It is conceivable for the same module to have a file called 'fibonacci.pyc' (or 'fibonacci.pyo' when -O is used) but no file called 'fibonacci.py'. This may be used to publish a Python code library that is relatively difficult to reverse engineer.
12. example
```python
import sys
# __debug__ is true by default, unless we run
# using -O (optimized code)
# python -O assert.py
print(__debug__)
# assert comes into affect only when __debug__ is true
num = int(input('Enter a positive number: '))
print(num)
assert(num > 0), 'Only positive numbers are allowed!'
def chkassert(num):
assert(type(num) == int)
chkassert('india')
sys.exit()
```
 <br />

## **Standard Modules** <a name="17.1"></a>

1.The Library Reference, which comes with Python, is a library of standard modules. The interpreter includes several modules that allow access to activities that are not part of the language's core but are included for efficiency or to enable access to operating system primitives such system calls.
2. example
```python
from math import *
print(fabs(-2.3))
print(factorial(5))
print(fmod(5, 2))
print(sqrt(25))
print(pow(2, 3))
print(pi)
```

 <br />
  
[go to Answers](#answers)

[go to List of Topics](#top)

<br />

## **Python Namespace** <a name="18"></a>

1. A namespace is a collection of identifiers that are stored in a container. Namespaces provide individual identifiers a sense of direction, making it feasible to distinguish between identifiers with the same exact name.
2. Namespaces in Python are specified by individual modules, and because modules can be housed in hierarchical packages, namespaces are also hierarchical.
3. When a module is imported, the names specified in the module are defined via that module's namespace and are accessed from calling modules by using the fully qualified name.
4. Examples include the collection of built-in names (functions like abs() and built-in exception names), global names in a module, and local names in a function invocation. A namespace is formed by the collection of attributes of an object.
5. Python searches the many levels of namespaces using the LEGB rule before locating the nameto-object mapping.
Local -> Enclosed -> Global -> Built-in, with arrows indicating the namespace-hierarchy search order.
- Local can be used within a function or a class method.
- Enclosed can refer to the function that is enclosing it, for example, if a function is wrapped inside another function.
- Global refers to the highest level of the executing script, and 
- Built-in are unique names reserved by Python for itself.
6. if a particular name:object mapping is not found in the local namespaces, the namespaces of
the enclosed scope is searched next. If the search in the enclosed scope is unsuccessful, too,
Python moves on to the global namespace, and eventually, it will search the built-in namespace
(if a name cannot found in any of the namespaces, a NameError is raised).
7. example
```python
lst = []
num = 10
def outer(n):
 lst.append(n)
 print(lst)
 global num
 num = 20
 print(num)
 def inner():
 num = 30
 print(num)
 return inner

func = outer(2)
func()
func = outer(3)
func()
print(num) 
```
 <br />

## **Python Packages** <a name="19"></a>

1. Packages are a method of organising Python's module namespace through the use of "dotted module names."
2. For instance, the module name C.D denotes a submodule named 'D' within a package named 'C.'
3. Just like using modules frees writers of various modules from having to worry about each other's global variable names, using dotted module names frees authors of multimodule packages from name collisions.
4. The __init .py is mostly used to initialise Python packages. The simplest approach to explain this is to examine the structure of a typical Python module.
```python
--+ PackageDemo
 |-- mod1.py
 |-- mod12Demo.py
 |-- mod2.py
 |-- __init__.py
```
5. The presence of the __init .py file in a directory signals to the Python interpreter that the directory should be handled as a Python package, as seen in the structure above. The '__init .py' file can simply be an empty file, but it can also execute package startup code or set the __all__ variable.
6. When using from package import item, the item can be a package submodule (or subpackage) or any other name declared in the package, such as a function, class, or variable. If the item is not declared in the package, the import statement assumes it is a module and attempts to load it. If it cannot find it, an ImportError exception is thrown.
7. If a package's __init .py' code includes a list called __all__, it is assumed to be a list of module names that should be imported when a from package import * is found. When a new version of the package is released, it is the responsibility of the package author to keep this list up to date. If package authors do not see a purpose for importing * from their package, they may choose not to support it.
8. If __all__ is not specified, the PackageDemo import * statement just guarantees that the package PackageDemo has been imported (perhaps by running its initialization code, '__init .py') and then imports whatever names are declared in the package. Any names specified by '__init .py' are included. It also contains any package submodules that were explicitly loaded by prior import lines.
 
9. file of mod1.py present in demo folder
 ```python
import demo.mod2
def f():
 global x
 x = 6
def getX():
 return x
def main():
 x = 5
 f()
 print(x)
 demo.mod2.g()
 x += 2
 print(x)
```
10. File of mod2.py present in demo folder
```python
import demo.mod1
def g():
 x = 10
 print(x)
 print(demo.mod1.getX())
```
11. File of mod12Demo.py present in demo folder
```python
from demo import *
if __name__ == '__main__':
mod1.main()

running script
 PS C:\Users\Documents\Training\code>python demo/mod12Demo.py
```

 <br />
  
[go to Answers](#answers)

[go to List of Topics](#top)

<br />
	
## **File Handling** <a name="20"></a>
  
### **Reading file** <a name="20.1"></a>
1. syntax for reading the file is
  open(file_name, mode)
  - The function open used to open the file and return the file object
  - mode are three types
    1. 'w' = write
    2. 'r' = read
    3. 'a' = append
2. example for file read
```
file_open = open("text.txt", "r")
print(file_open.read())
```
  
3. file read using loop
```python
file = open ("test.txt",'r')
for line in file:
  print(line, end='')
file.close()

Explaination of code
A newline character is already present in line print read from file. To prevent publishing two lines, override the default end argument after each line, newline characters.
 
running code
PS C:\Users\Documents\Training\code> python file_handling.py  
  
output
I need to learn python
I like programming 
```
 
### **Writing and appending to file** <a name="20.2"></a>
  
```python 
file = open("test.txt", "w") #writing
file.write("I like teaching")
file.close()
  
running code
PS C:\Users\Documents\Training\code> python file_handling_writing.py    
  
output seen in file
I like teaching 
```
```python 
file = open("test.txt", "a") #appending
file.write("I like playing games")
file.close()
  
running code
PS C:\Users\Documents\Training\code> python file_handling_appending.py   
  
output seen in file
I like teaching I like playing games
```

 ### **Deleting file** <a name="20.3"></a>
 ```python
import os 
os.remove("test.txt") #The file test.txt will be removed form the folder.
```  

 <br />
  
[go to Answers](#answers)

[go to List of Topics](#top)

<br />

### **Important functions and points for file handling** <a name="20.4"></a>
  
function | represents 
:----- | :----: 
readline() | Read the contents from the file until it finds newline or end of file and returns a single string
write(s) | Write the string s into the file
close()| Flush the buffer and close the file
  
1. The Python operating system module has methods for performing file-processing actions such as renaming and removing files.
2. To use this module, first import it, and then use any relevant functions.
  - The rename() function accepts two parameters: the current filename and the new filename.
  - You can delete files by passing the name of the file to be destroyed as an argument to the remove() function.
  - The os module has numerous methods for creating, removing, and changing directories.
  - To create directories in the current directory, use the os module's mkdir() function. This procedure requires an argument containing the name of the directory to be created.
  - To change the current directory, use the chdir() technique. The chdir() function accepts one argument, which is the name of the directory to be made the current directory.
 - The getcwd() function returns the path to the current working directory.
 - The rmdir() function deletes the directory that is supplied as an argument. Before eliminating a directory, it is necessary to delete all of its contents.
  
   
 <br />
  
  
 ### **Exercise-14** <a name="20.5"></a> 
  
 1. Write a script that reads the first 10 lines from the file. Take any file you wish that contain minimum 30 lines.
 2. Write a script that count the number of lines in a file. Take any file you wish
 3. Write a script that write lines to the file and they are
 ```python
1. Steve Jobs is a popular name in the world.
2. He was the co-founder and chairman of Apple Inc.
3. He is also referred to as an industrial designer, investor, and media tycoon.
4. His full name was Steven Paul Jobs.
5. He was born on 24th February in the year 1955.
```
4. Write a script that append lines to the file that are created in problem 3 and they are
```python
1. Steve Paul Jobs is regarded as a successful American businessman.
2. He had attained success in different fields.
3. He had a great contribution to the development of computers and mobiles.
4. He is stated as the initiator of the personal computer revolution.
5. He had served as the CEO of Apple Inc from 1997 to 2011.
```
  <br />
  
[go to Answers](#answers)

[go to List of Topics](#top)

<br />
  
## **Exception Handling** <a name="21"></a> 
  1. python handles when the error/exception are occured in code by printing error message. 
  2. In try code it will check whether the code has errorsd
  3. In except code it will handles the code by printing the error message.
```python
from sys import argv
try:
    addition = float(argv[1]) + float(argv[2])
    print("The additon is", addition)
except:
    print("Error: Provide two numbers")
  
running script
PS C:\Users\Documents\Training\code> python exception_handling.py suresh haresh
  
output
Error: Provide two numbers
```

 <br />
  
 ### **Exercise-15**   <a name="21.1"></a> 
 1. Write a script that join two strings and input is given by the user. When the user gives numbers the error should be handled.
 ```python 
 example two strings are Multiple Wishes -  output is MultipleWishes
 example user gives numbers are 1 5 - output is "Error: Provide two strings"
 ```
 2. Write a script for multiplication of two numbers(int or float) and the input is taken from the user. When the user gives strings the error should be       handled.
```python
example two numbers are 2 5 - output is 10
example user gives are happy life - utput is "Error: Provide two numbers"
```


## **Python Buildtool**  <a name="22"></a> 

1. These libraries aid in Python development by allowing you to walk through code, inspect stack frames, and set breakpoints, among other things.
2. The pdb module defines an interactive Python source code debugger. It allows you to establish (conditional) breakpoints and single step at the source line level, inspect stack frames, list source code, and evaluate arbitrary Python code in the context of any stack frame.
3. The debugger is extendable; in fact, it is specified as the class Pdb. The modules bdb and cmd are used in the extension interface.
4. The prompt from the debugger is (Pdb). pdb.py may also be used to debug other scripts as a script.
```python
 PS C:\Users\Documents\Training\code>python -m pdb addition.py
```
5. s(tep) - Execute the current line, stopping at the first feasible opportunity (either in a called function or on the next line in the current function).
6. n(ext) - Continue execution until the current function's next line is reached or it returns. (The distinction between next and step is that step stops within a called function, whereas next runs called functions at (near) full speed, pausing only at the next line in the current function.)
7. unt(il) - Continue execution until a line with a line number larger than the current one is reached, or until the current frame is returned.
8. r(eturn) - Keep running until the current function returns.
9. c(ont(inue)) - Continue execution, stopping only when a breakpoint is reached.
[first[, last]] l(ist] - Display the source code for the currently selected file. List 11 lines surrounding the current line or continue the previous listing without arguments. List 11 lines that are centred on one argument. List the specified range using two parameters; if the second argument is smaller than the first, it is understood as a count.
11. a(rgs) - Print the current function's argument list.
12. p(rint) expression - Evaluate the expression and print its value in the current context.
13. execute [args...] - Run the debugged Python programme again (with without an argument). Breakpoints, actions, and debugger choices are all saved. "restart" is an abbreviation for "run."
14. q(uit) - Exit the debugger. The currently running programme is terminated.
15. The distutils package allows you to generate and install new modules into your Python system. The new modules may be entirely Python, extension modules written in C, or collections of Python packages including modules written in both Python and C.

16. As a programmer, we should do is
 - generate a source distribution 
 - write a setup script (setup.py by standard) 
 - (optionally) write a setup configuration file
 - Create one or more built (binary) distributions (optional).

<br />

	
[go to Answers](#answers)

<br />

[go to List of Topics](#top)

<br />
	
## **Answers**

### Exercise - 1 <a name="E-1"></a>

1. C
2. D
3. A, B, C
4. Solution Code

```python
#output

wonders_of_world = 7
print(wonders_of_world)
```

5. Solution Code

```python
#output

planet_near_to_sun = "Mercury"
print(planet_near_to_sun)
```

6. B

  <br />
  
### Exercise - 2 <a name="E-2"></a>

1. student_name = "Ramesh"
2. Solution Code

```python
#output

number1 = 10
number2 = 5
number3 = number1 + number2
print(number3)

```

3. Solution Code

```python
colour = "blue"
fruit = "Mango"
number = 22
article = "is"

print("sky", article, colour +",", fruit, article, "yellow, age of suresh",  article, number , ".")
```

  <br />
  
### Exercise - 3 <a name="E-3"></a>

1. Solution code

```python
number1 = int(input("Enter the first number "))
number2 = int(input("Enter the second number "))

multiplication = number1 * number2
print("The multiplication of two numbers is", multiplication)
```

2. Solution code

```python
from sys import argv

name = argv[1]

print(name, "is very good boy who helps everyone and also",name, "participates in all the sports and cultural meet.", name, "hobbies are playing virtual games and also watching movies.")
```

3. Solution code

```python
base = float(input("Enter the base of the triangle "))
height = float(input("Enter the height of the triangle "))

area_triangle = (base * height) / 2
print("The area of triangle is ", area_triangle)
```

4. Solution code

```python
name = argv[1]
year = argv[2]
name_of_college = argv[3]
lives = argv[4]


print("student_name :", name)
print("class        :", year)
print("college_name :", name_of_college)
print("city_lives   :", lives)
```

 <br />
 
### Exercise - 4 <a name="E-4"></a>

1. A
2. B
3. B
4. 12 4
   True
   False
   False
5. False

 <br />
 
### Exercise - 5  <a name="E-5"></a>

1. Solution code

```python
string = "python"
print(string.upper())
```

2. Solution code

```python
string = "Cython"

result = string.replace("C", "P", 1)
print(result)
```

3. Solution code

```python
string = "Python"

result = string.center(14,"*")
print(result)
```

4. 1

<br />

### Exercise - 6 <a name="E-6"></a>

1. Solution code

```python
print("Talk is \'cheap\'. Show me the code.")
print("I\'m not a \"great\" programmer!I\'m just a \t good programmer with great habits.")
print("If your ship doesn \'t come in, \\swim\\ out to it?")
```
