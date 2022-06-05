# SSSSO-RR-District-Basic-Python-Training-June-2022
Basic Python Training Organized by Sri Sathya Sai Seva Organization RR District in the month of June 2022.

## Timings
1. Saturday - Evening - 6pm to 8pm
2. Sunday - Morning - 8am to 10am

> Total - 4 hours of training sessions per week

# Setting up git and github, python 3.10, VS Code
1. [programming knowledge channel - How to Install Git on Windows 10 + Setting Up Git and GitHub on Windows 10](https://www.youtube.com/watch?v=bb_LoXAC-zE)
2. [How to install python 3.10 on windows 10/11](https://www.youtube.com/watch?v=AwIXfaGEN4c)
3. [How to install visual studio code on windows 10/11](https://www.youtube.com/watch?v=JPZsB_6yHVo)

## List of Topics that will be covered under this training <a name="top"></a>

1. [Let's begin the Python Show](#1)
	* [History of Python](#1.1)
	* [What is Python](#1.2)
	* [Applications of Python](#1.3)
	* [How does Python Programming Language support a Complex Problem Decomposition](#1.4)
	* [What is an interpreter](#1.5)
	* [How To Open and Run the Interpreter Which is installed](#1.6)
	* [Comparison of python with other Languages](#1.7)
	* [Famous and Most used versions of python](#1.8)
	* [Why should we learn Python](#1.9)
2. [About Python](#2)
	* [Writing python scripts in a file and running it in the command line
	interface](#2.1)
	* [Commenting in python](#2.2)
	* [Print function](#2.3)
	* [Header for Python script](#2.4)
	* [Indentation](#2.5)
	* [Continuation lines](#2.6)
3. [Variables](#3)
	* [Python Variables](#3.1)
	* [Naming conventions of variables](#3.2)
	* [Creating good names](#3.3)
	* [Exercise-1](#3.4)
4. [Data Types](#4)
	* [Integers](#4.1)
	* [Floating point](#4.2)
	* [Complex](#4.3)
	* [boolean](#4.4)
	* [Conversion of one data type to another](#4.5)
	* [Exercise-2](#4.6)
5. [User Input](#5)
	* [Input function](#5.1)
	* [Command line parameters](#5.2)
	* [Exercise - 3](#5.3)
6. [Escape sequences](#6)
    * '\n' - [Newline character](#6)
    * '\r' - [Return character](#6)
    * '\b' - [Backspace character](#6)
    * '\\' - [Backslash character](#6)
    * '\”' - [Double quote character](#6)
    * '\’' - [Single quote character](#6)
    * '\t' - [Tab character](#6)
    * '\a' - [Alarm character](#6)
    * [Exercise - 4](#6.1)
7. Operators
	* Numeric 
	* Comparison
	*  Identity
	* Membership
	* Assignment
	*  Logical
8. Conditional statements
	* If
	* If else
	* Nested If elif else
9. Loops
	* While
	*  for
10.  Lists
	* list comprehension 
11. Tuples 
12. Dictionaries
13. File Handling
	* Read 
	*  Write
	* delete
14. Functions
15. Exception Handling
16. Modules
17. Namespace
18. Packages
19. Built in tools
20. repr()
21. difference between running the code in vs code and jupyter notebook
22. assert (basic debugging) - to set a breakpoint
23. What editors are required to use in python 

## **1. Let's begin the Python Show** <a name="1"></a>

### **History of Python** <a name="1.1"></a>

**Python** was developed by ***Guido van Rossum*** and was released first on **February 20, 1991** (31 years ago). It is one of the most widely-used and loved programming languages. It is also a **free** and **open-source language** with very simple and clean syntax.

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
  >OpenCV, Pillow, SimpleITK are some libraries of image processing .
  
- Web frameworks and applications.
  >Django, Flask, TurboGears, web2py and some other Python web framework are used for Python Web development.

- Business applications 
  > Python is also used to build ERP and e-commerce systems like Oodo, Tryton, OpenERP.

- Operating Systems
  >Linux, FreeBSD, Windows, macOS are the operating systems.

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
	* So, The cycle is slow. You need to develop **software** more quickly. Possibly, perhaps you have written a program that could use an **extension language**, and you do not want to design a language, write and debug an interpreter for it, then tie it into your application.

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
    - press ```ctrl+d``` or ```ctrl+z``` or ```type exit()``` to exit the interpreter.

	  - If you have **Visual Studio Code** installed, at the top of the VS Code window, click on the **Terminal** option. And then click on the **New Terminal** option.

    - > In Visual Studio Code : Terminal > New Terminal

2. When commands are read from a **tty**, the interpreter is said to be in **interactive** mode. In this mode it prompts for the next command with the primary prompt, usually three greater-than signs **(‘>>> ‘)**. ```>>>``` this symbol is called as ```chevron prompt```. It means that python interpreter is in ```interactive mode```, waiting for user input.
 
3. For continuation lines it prompts with the secondary prompt, by default three dots **(‘...’)**. The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt. The symbol ```...``` in this context, should not be compared (or) correlated with ```... <ellipsis>``` operator of python.

4. Continuation lines are needed when entering a multi-line construct. As an example, look at this if statement:

![](https://github.com/saikrishnavadali05/python3_ebook/blob/master/Images/Screenshot%202022-01-31%20110438.jpg?raw=true)


### **Comparison of python with other Languages?** <a name="1.7"></a>
  
Column | Python | Java   | C++    | C 
:----- | :----: | -----: | :----: | -----:
Code Executor | Interpreter| Compiler | Compiler | Compiler
Learning and Coding Difficulty Level | Very Easy | Medium | Medium  | Difficult
Number of Lines of Code (SLOC)  | Very less  | Less | Many | Extremely Many
Costs incurred to Build Applications  | Less Expensive  | Expensive | More expensive  | Most expensive
Availability of Learning and Reusable Resources  | Very High  | High | Less  | Less
  
<br />

[go to List of Topics](#top)

<br />
 
### **Famous and Most used versions of python?** <a name="1.8"></a>

There are multiple versions of python since its inception. 
Out of which, versions after ```Python 3.4 ``` are the most widely used ones.

1. 1989, Implementation of Python as a successor of ```ABC Programming Language``` started.
2. 1991, Python 0.9
3. 1994, Python 1.0
4. 2000, Python 2.0 (was popular, but no longer supported since Jan 1, 2020).
5. 2008, Python 3.0 (Famous)
6. 2022, Python 3.10 (Very Very Famous and Huge Developer Community)

* The main difference between version 2 and version 3 is **the stablity of the code has increased a lot** and there were a few changes in the syntax and also increase in **speed of execution of code**. So, Now version 2 has no support or resources so everyone should have latest version in their Local system.
  
 <br />

### **Why should we learn Python?** <a name="1.9"></a>
  
1. By the **start** of 2022 :
**PyPi** (Python Package Index) has > **3,50,000** Python packages (almost all of them are free and open source).
10 million+ (1 crore+) python developers are flourishing all around the world (Huge python developer community).

2. In the mid of 2021 :
**6,200** companies (around the world) have used (90% of their code is written only in) Python for their platforms.
**10,000+** Python job ads on **Glassdoor**.
**14,000+** Python openings on **Indeed**.

3. The number might have **doubled** by now (i.e., June 2022).

4. A Rapid growth is being observed in the world of Python.
Because, Python is **very easy to read, write and understand**.
Learning Python is not as difficult as it looks, but it’s definitely **worth your efforts**.
  
5. In #india, python developers are being paid well... What is the reason?

		4.27 lpa ----> 9.09 lpa ----> 11.5 lpa

6. The following are the average salaries based on different **experience** levels
	*	The average salary of an ***entry-level*** Py developer - ***₹427,293****.
	*	The average salary of a ***mid-level*** Py developer - ***₹909,818***.
	*	The average salary of an ***experienced*** Py developer - ***₹1,150,000***.

7. *The reason is simple and straight forward*. Many of the top companies use python extensively. The following list contains, but not limited to only software companies. In fact, python is being used even by Bio-scientists, Chemical Scientists, etc..

8. Examples of companies that use Python extensively are

> Top Financial Companies
* Goldman Sachs
* JP Morgan Chase
* PayPal

> Large Tech Companies
* Google #google
* Dropbox #dropbox
* Netflix #netflix
* Meta #Meta (Facebook), #instagram
* Uber
* Twilio
* Mozilla
* Reddit
* Increment

> US Government Agencies
* The Consumer Financial Protection Bureau (CFPB)
* NASA
* United States Central Intelligence Agency (CIA)
* Securities and Exchange Commission (US SEC)
* Department of the Navy and National Institute of Standards and Technology (NIST)

> Important Multi National Companies that use python extensively
* Nokia, HPE, Dell, Novell, emc2, vmware, mindtree, OLA, Persistent, GSLabs, Macropace, Xentrix, etc

The list goes on and on... all of them use python extensively.
Python programmers are very high in demand now-a-days..

> One easy way to become rich in the software industry is to learn and perform : **web development using python**.

9. Web Development using Python :
* Python
* Django / Flask
* HTML
* CSS
* JavaScript

The best and most productive field to flourish today is **web development** using python. Which is also popularly known as **Full Stack Python**

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
  
  1. Comments are text portions that clarify what the program does and how it functions. 
  2. The character used for commenting is #.
  3. The Python interpreter ignores the following text from where the character # starts.
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
  
  1. This is the baisc function which is used to print the content on the screen. This function always give a new line
  2. Syntax for the **print** function
		>print (objects, sep = ':', end = '\n')
	    * objects can be more than one.
	    * Here, **sep** and **end** are **optional**. **sep** is used to seperate objects and **end** is used to tell what it should do at the end of statement.
3. Examples of the print function are
      ```python
        print("My name is Ramesh", "studying in IIT")
      ```      
   *  From the above print statement "My name is Ramesh" is expression -1 and "studying in IIT" expression -2.
   * Prints the expressions with spaces between them
      ```python
         print("My name is Ramesh", "studying in IIT", sep=':', end=' ')
      ```
  
   *  Prints the expressions with : between them and also new line is avoided from end.
  
4. After executing the two print statement examples the answers are
       <img src="https://github.com/Vissamsetty-Bharathrath/python3_ebook/blob/master/Training/19.jpg" alt="Print function" width="600"/>
  
   <br />
   
 ### **Header for Python script** <a name="2.4"></a>
  
  1. The header is very important for the program because when anybody wants to understand your program or if you want to revise this program in the future the header will be very helpful to tell how code works.
  
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
multiply = number1 * number2
div = number1 / number2
expo = number1 ** number2

print("The results are")
print("addition ", add)
print("substraction ", sub)
print("multiply ", multiply)
print("division ", div)
print("exponentation ", expo)
``` 

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
```
<br />
   
### **Indentation** <a name="2.5"></a>

  1. **Indentation** plays a very important role in writing **python script**.
  2. The meaning of indentation is the proper **arranging** of the lines of code in the script.
  3. For arranging we can either use **Tab** or **Space**. But the right way is to use Tab which makes our code to write easily.
  4. Now let's understand with an example
  
  ```python
# Convert the command line parameters to numbers
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
  
 * running script
> PS C:\Users\Documents\Training\code> python indentation.py 

```console
# output
  
10 - 7 = 3
```
  
  From the above example, we can see there is a white space after the **if** line it is given because the lines should be executed only when the 'If' condition satisfies. Similarly for the 'else' condition. 
  
<br />
  
 ### **Continuation lines** <a name="2.6"></a>
 
  1. If we are writing one big statement that occupies more than one line then we will be using this character \\. 
  2. This character \ should be the end of the line.
  3. For example 
   ```python
     print("My company \
     name is \
     Multiple Wishes.")
   ```
   when we run the script the output is
   <img src="https://github.com/Vissamsetty-Bharathrath/python3_ebook/blob/master/Training/11.jpg" alt="Continuation lines" width="600"/>

<br /> 
   

## **Variables** <a name="3"></a>
  
### **Python Variable** <a name="3.1"></a>

1. **Variable** is a name that is used to refer to **memory location**. 
2. Python variable is also known as an identifier and used to hold value. Variable names can be a group of both the letters and digits, but they have to begin with a letter or an underscore.No need to mention the datatype of the variable because python automatically detects the type of the variable. 
3. Variables names are case sensitive for example they are two variables **amount** and another variable is **Amount**. Both the variables are different.
 
```python
x = 10
_x = 20
```
Here the variable 'x' and '_x'refers to an integer object.
Examples of variables are
```python
name = 'Ram'
Weight = 60
height = 80.50
```

We can get the data type of any object by using the type() function:
Example : 
```python
Print the data type of the variable x:

>>> x = 5
>>> print(type(x)) 
<class 'int'>
>>>
```
Here we get output as <class 'int'> because integer value is assigned to variable.

<br />
  
### **Naming conventions of variables** <a name="3.2"></a>
  
They are two types we can create a variable name
  1. Snake Case : This looks like instead of space we use underscore(_). For example is **name_of_the_student**
  2. Camel Case : This looks like for each new word it starts with capital letter. For example is **NameOfTheStudent**
  3. My view : In my view I prefer to use Snake case because it is easy to understand and also it is recommended by organization of python. 
  
<br />

### **Creating good names** <a name="3.3"></a>

1. Variable names should have **meaningful** and also it should **represent something**.
2. Meaningful variable names can make our **code more readable**, **easier to debug code** and also **maintain it**. 
3. Examples:  
   -  n  -                    do not know what is n
   -  name   -                able to understand but what name
   -  name_of_the_student  -  yes, very easy to understand
  
<br />

### **Exercise-1** <a name="3.4"></a>

  1. Create a variable as **student_name** and assign the value as **Ramesh** to the variable.
  2. given the problem to substract 5 and 10, using variables: number_1 and number_2. fill in the below code as
  ```python 
  _  =  _
  number_2 = _
  print(x _ y)
  ``` 
  3. Write a script that defines the following variables
  ```python
  colour = "blue"
  fruit = "Mango"
  number = 22
  article = "is"
  ```
use the variables above to print the following statements exactly 
sky is blue,
Mango is yellow,
age of suresh is 22.
  

<br />
  
## **Data Types** <a name="4"></a>

1. **Variables** can hold values, and every value has a data-type. 
2. **Data-types** in Python can be either mutable or immutable. 
3. A mutable object can be changed after it is created, and an immutable object cannot. Objects of built-in types like (int, float, bool, str, tuple, frozenset) are immutable. Objects of built-in types like (list, set, dict) are mutable. Custom classes are generally mutable.

|  Class | Description |Immutable  |
| ------ | ------ | ------ |
| bool |Boolean value  |Yes  |
| int |Integer  |Yes |
|float  |Float point number  |Yes |
| list |Mutable sequence of objects  |No |
|tuple  | Immutable sequence of objects |Yes |
| str |Character string  |Yes
| dict |Associative mapping (dictionary)  |No |
| set |Unique set of values  |No |
| frozenset | Immutable form of set |Yes |

<br />
  
### **Integer data type** <a name="4.1"></a>

1. The **integer** data type has only numbers without decimals in it. The numbers are either positive or negative.
2. Examples:
```python
    No_of_wickets = 5
    overs_bowled = 4
```
<br />

### **Floating-point data type** <a name="4.2"></a>

1. The **floating** point data is the having decimal point after integers.
2.  2. Examples:
```python
strike_rate_of_batsman = 105.45
economy_of_bowler = 6.25
```
3. we can also represent the floating point with  **e** or **E**. **e** **E** means is the power of 10.
```python
strike_rate_of_batsman = 80e5
economy_of_bowler = 24E3
overs_bowled = 4.3
```
  * After we print the above variables the answers are
    <img src="https://github.com/Vissamsetty-Bharathrath/python3_ebook/blob/master/Training/21.jpg" alt="Floating_data_type" width="500"/>
  
<br />

### **Complex data type** <a name="4.3"></a>

  1. The **complex** data type is has an imaginary part in it. The imaginary part is represent with **j**.
  2. Examples
  ```python
  a = 3+7j
  b = 5-9j
  ```
 <br />
 
### **Boolean data type** <a name="4.4"></a>

  1. It has two values True and False
  2.  Examples
  ```python
  ram_age = 25
  shyam_age = 12
  print(ram_age > shyam_age)
  print(ram_age < shyam_age)
  
  Output
  True
  False
  ```    

<br />

### **Conversion of one data type to another** <a name="4.5"></a>

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
 
 
### **Exercise - 2** <a name="4.6"></a>

  1. Tell the given type of the variable 
  ```python
  name = "Mahesh"
  type(name)  
    
  A. int
  B. <class 'int'> 
  C. <class 'str'>
  D. string
  ```
  2. which method is ised to find the type of the variable for **a = 20**
  ```python
  A. print(i)
  B. int(i) 
  C. str(i)
  D. type(i)
  ```
  3. Tell the correct answers from the following
  ```python
  A. a = "10"
  B. b = "ram21" 
  C. c = 12
  D. 1_d = 6 
  ```
  4. assign the value to the variable and print it.
  ```python
  wonders_of_world = 
  print()
  ```
  5. write a word in the for the variable and print it 
  ```python
  planet_near_to_sun=
  print()
  ```
  6. Write the scientific notation for given float number 0.002569 is
  ```python
  A. 2569e-5
  B. 2.569e-3
  C. 256.9e-4
  D. 0.2569e-6 
  ```
  <br />

## **User input** <a name="5"></a>

  1. They are two methods where user can give input and they are using input function and another one is using command line parameters.

### **input function**  <a name="5.1"></a>
 
  3. the input functions always gives only string. whatever the input given by the user the input function changes into string.
  
  Examples for **input function** 
  ```python
  name_of_user = input("Name of the user: ")
  print(type(name_of_user))
  print(name_of_user)
  age_of_user = input("Age of the user: ")
  print(type(age_of_user))
  print(age_of_user)
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
  
 
### **Command line parameters** <a name="5.2"></a>

 1. Command line parameters are also called as Command line arguments.
 2. The values or parameters are provided in the command to run the program.
 3. A list of strings named **argv** is provided inside the code for values.
 4. Each value given in the command is consider as string and also have infinite number of values that are separated with spaces.
 5. To use **argv** we should import the module into the script
 ```python
  from sys import argv
  ```
 6. The variable ```argv[n]``` may be used to access each command line parameter in our program.
     - Here n is index of the value.
     - ```argv[0]``` is script name and ```argv[1]```, ```argv[2]```, etc are contains values.
     - Example
      PS C:\Users\Documents\Training\code> python test.py Ram 15 70.45
        1. test.py is ```argv[0]```
        2. They are three command line parameters
          - Ram is ```argv[1]```
          - 15 is ```argv[2]``` 
          - 70.45 is ```argv[3]```
    
  Examples for **command line parameters**
  Python script
  
  ```python
    from sys import argv
    num1 = argv[1]
    num2 = argv[2]
    num3 = int(argv[3])
    num4 = int(argv[4])
    add1 = num1 + num2
    add2 = num3 + num4
    print("The total add1 is", add1)
    print("The total add2 is", add2)
  ```
  running script
    
  > PS C:\Users\Documents\Training\code> python command_line_parameter.py  10 20 30 40
    
  ```console
  # output
    
  The total add1 is 1020
  The total add1 is 70
  ```
  1. From the above script we have things to remember are
      * By default **argv** consider any value as string so if we specify the data type properly at the time of assigning then it can be worked as the result we thought.
     
 <br />
    
 ### **Exercise - 3** <a name="5.3"></a>
 
 1. Write the script asking the user to give two integers and multiply them 
 2. Take the command line parameter any name you want (C:> C:\Users\Documents\Training\code> python command_line_parameter.py Girish and print in the following paragraph.
```python    
Girish is very good boy who helps everyone and also Girish participates in all the sports and cultural meet. Girish hobbies are playing virtual games and also watching movies.
```
 3. Write the script for calculating area of trainagle ( ask user to enter base and height).
 4. Write the script of the student form(name_of_student, class_studying, college_name, city_lives) that accepts as command line parameters and prints as
 ```python
  student_name : Hareesh
  class        : 12th
  college_name : SSB
  city_lives   : Hyderabad
 ```
    
 <br />

 ## **Escape sequences** <a name="6"></a>
  
  1.  The character **\\** represents the beginning of an escape sequence.
  2. Table of escape sequence
  
Sequences | represents 
:----- | :----: 
\b | backspace
\n | newline
\t | tab
\r | return
\a | bell
\\\ | backslash
\\" | double quote
\\' | single quote
  3. examples of escape sequences statements
  <img src="https://github.com/Vissamsetty-Bharathrath/python3_ebook/blob/master/Training/20.jpg" alt="Escape Sequences" width="500"/>
    
<br />

  
### **Exercise - 4** <a name="6.1"></a>

  1. Write a script to print the following statements using print statement
  
    - Truth can only be found in one place: the code.
    - You have baked a really lovely cake, but then you have used dog shit for frosting.
    - On two occasions, I have been asked [by members of Parliament], Pray, Mr. Babbage, if you put into the machine wrong figures, will the right answers come out?
  
  2. Write a script to print the following statements using escape sequences
  
    - "Talk is 'cheap'. Show me the code."
    - "I'm not a great programmer! I'm just a good programmer with great habits."
    - "If your ship doesn’t come in, swim out to it?"
  
  3. write a script to print the following shape using print statement
  ```python
           * 
       * python * 
     * is  *  a    * 
   * good  * programming * language * 
 * to * learn * for * beginners * 
 ```
  4. Write a script to print the following menu using escape sequences and ring the bell sound when the order has finished printing **Thank you, Visit Again!!!!!**.
  
  <img src="https://github.com/Vissamsetty-Bharathrath/python3_ebook/blob/master/Training/22.jpg" alt="Escape Sequences" width="300"/>
  
  <br />
