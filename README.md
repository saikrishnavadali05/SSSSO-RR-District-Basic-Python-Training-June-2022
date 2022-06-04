# SSSO-RR-District-Basic-Python-Training-June-2022
Basic Python Training Organized by Sri Sathya Sai Seva Organization RR District in the month of June 2022.

## Timings
1. Saturday - Evening - 6pm to 8pm
2. Sunday - Morning - 8am to 10am

# Setting up git and github, python 3.10, VS Code
1. [programming knowledge channel - How to Install Git on Windows 10 + Setting Up Git and GitHub on Windows 10](https://www.youtube.com/watch?v=bb_LoXAC-zE)
2. [How to install python 3.10 on windows 10/11](https://www.youtube.com/watch?v=AwIXfaGEN4c)
3. [How to install visual studio code on windows 10/11](https://www.youtube.com/watch?v=JPZsB_6yHVo)

## List of Topics that will be covered under this training
1. Start up for python Language
1. Installation of python
2. What editors are required to use in python 
2. About Python
1. History
2. Comparison of py with another language
3. Versions of python
4. Indentation
5. Continuation lines
6. Command line interface coding
7. Writing python scripts in a file and running it in the command line 
interface.
8. Commenting in python
9. Debugging the code 
10. Print function
3. Escape sequences
    * '\n' - Newline character
    * '\r' - Return character
    * '\b' - Backspace character
    * '\\' - Backslash character
    * '\”' - Double quote character
    * '\’' - Single quote character
    * '\t' - Tab character
    * '\a' - Alarm character
4. Data Types
1. Integers
2. Floating point
3. Complex
4. String
5. bool
5. User Input
1. Input function
2. Command line parameters
6. Operators
1. Numeric 
2. Comparison
3. Identity
4. Membership
5. Assignment
6. Logical
7. Conditional statements
1. If
2. If else
3. Nested If elif else
8. Loops
1. While
2. for
9. Lists
1. Read
2. Write
3. delete
10. Tuples
11. Dictionaries
12. Functions
13. File Handling
14. Exception Handling
15. Modules
16. Namespace
17. Packages
18. Built in tool
19. list comprehension
20. repr()
21. difference between running the code in vs code and jupyter notebook
22. assert (basic debugging) - to set a breakpoint


### **What is Python?**
<span style="color: blue;">**Python** is a general-purpose high-level programming language. Being a general-purpose language, it can be used to build almost any type of application with the right tools/libraries. Its standard library is large and comprehensive. This makes it easy developers to learn python. Additionally, python supports objects, modules, threads, exception-handling, and automatic memory management which help in modelling real-world problems and building applications to solve these problems. Python is also used in Machine Learning, Artificial Intelligence, Web Development, Web Scraping, and various other domains.</span>

<br />

### **Applications of Python?**
<span style="color: blue;">Python has grown to become part of web-based, desktop-based, graphic design, scientific, and computational applications.

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
  > 
- Software Development

  >Scons, Buildbot, Apache Gump, Round up, Trac.

<br />
  
### How do programming languages support problem decomposition?

<span style="color: blue;">Python supports multiple programming paradigms and features a fully dynamic type system and automatic memory management, similar to Perl, Tcl etc. Like other dynamic languages, Python is often used as a scripting language.

<span style="color: blue;">If you have to work with several C libraries, and the usual C write/compile/test/re-compile cycle is slow. You need to develop software more quickly. Possibly, perhaps you have written a program that could use an extension language, and you do not want to design a language, write and debug an interpreter for it, then tie it into your application.

<span style="color: blue;">Python allows you to split up your program in modules that can be reused in other Python programs. It comes with a large collection of standard modules that you can use as the basis of your programs. There are also built-in modules that provide things like file I/O, system calls, sockets, and even interfaces to graphical user interface toolkits like Tk.

<br />

### What is an interpreter?
<span style="color: blue;">An interpreter is a program that reads and executes code. This includes source code, pre-compiled code, and scripts. Common interpreters include Perl, Python, and Ruby interpreters, which execute Perl, Python, and Ruby code respectively. 

<span style="color: blue;">If we write a Python code in a text file with a name like hello.py. How does that code Run? There is program installed on your computer named "python3" or "python", and its job is looking at and running your Python code. This type of program is called an "interpreter".

<br />

### How To Get An Interpreter?
<span style="color: blue;">There are 2 easy ways to get the interpreter:

  - <span style="color: blue;"> Open a command-line terminal. Mac: run the "Terminal" app in the Utilities folder. Windows: type "powershell" in the lower left, this opens the Windows command line terminal. In the terminal type the command "python3" ("python" on Windows, or sometimes "py"). This runs the interpreter program directly. On the Mac type ctrl-d to exit (on Windows ctrl-z).

  - <span style="color: blue;"> If you have PyCharm installed, at the lower-left of any window, click the Python Console tab. Or use the Tools > Python Console menu item to open an interpreter window within PyCharm.

<span style="color: blue;"> When commands are read from a tty, the interpreter is said to be in interactive mode. In this mode it prompts for the next command with the primary prompt, usually three greater-than signs (‘>>> ‘); for continuation lines it prompts with the secondary prompt, by default three dots (‘...’). The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt.

<span style="color: blue;"> Continuation lines are needed when entering a multi-line construct. As an example, look at this if statement:

![](https://github.com/saikrishnavadali05/python3_ebook/blob/master/Images/Screenshot%202022-01-31%20110438.jpg?raw=true)


### Comparison of python with other Languages?
  
Column | Python | Java   | C++    | C 
:----- | :----: | -----: | :----: | -----:
Compilation | Interpreter| Compiler | Compiler | Compiler
Learning and coding Difficulty level | Very easy to learn  | difficult | difficult  | difficult
Lines of Code  | Very less  | less lines | more lines  | bulk of lines
Cost incurred in project building  | Very less expensive  | expensive | more expensive  | most expensive
Resource Requirement  | Many resources  | less compared to python | less  | less
  
<br />
 
### Versions of python?
They are two versions
1. Version 2
2. Version 3

* The main difference between version 2 and version 3 is stablity of the code increases and they are some changes in the syntax and also increase in speed of execution of code. So, Now version 2 has no support or resources so everyone should have latest version in their Local system.
  
 <br />

### Major implementations of python

> CPython, PyPy, Stackless Python, MicroPython, CircuitPython, IronPython, Jython.

### Why should we learn Python?
  
By the start of 2022 :
PyPi (Python Package Index) has > 3,50,000 Python packages (almost all of them are free and open source).
10 million+ (1 crore+) python developers are flourishing all around the world (Huge python developer community).

In the mid of 2021 :
6,200 companies (around the world) have used (90% of their code is written only in) Python for their platforms.
10,000+ Python job ads on Glassdoor.
14,000+ Python openings on Indeed.

The number might have doubled by now (i.e., Feb 2022).

A Rapid growth is being observed in the world of Python.
Because, Python is very easy to read, write and understand.
Learning Python is not as difficult as it looks, but it’s definitely worth your efforts.
  
In #india, python developers are being paid well... What is the reason? click to see more...

4.27 lpa ----> 9.09 lpa ----> 11.5 lpa

The average salary of an entry-level Py developer - ₹427,293.
The average salary of a mid-level Py developer - ₹909,818.
The average salary of an experienced Py developer - ₹1,150,000.

The reason is simple and straight forward. Many of the top companies use python extensively. This list contains but not limited to only software companies. In fact, python is being used even by Bio-scientists, Chemical Scientists, etc..

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

> Government Agencies
* The Consumer Financial Protection Bureau (CFPB)
* NASA
* United States Central Intelligence Agency (CIA)
* Securities and Exchange Commission (US SEC)
* Department of the Navy and National Institute of Standards and Technology (NIST)

The list goes on and on... all of them use python extensively.
Python programmers are very high in demand now-a-days..

> Easy way to become rich
A person can become very rich in software industry if he is an expert in web development using python.


Web Development using Python :
* Python
* Django / Flask
* HTML
* CSS
* JavaScript

The best and most productive field to flourish today is web development using python.
   
## References

1. https://www.jython.org/
2. https://en.wikipedia.org/wiki/Jython
3. https://en.wikipedia.org/wiki/Python_(programming_language)#
