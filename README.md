# SSSSO-RR-District-Basic-Python-Training-June-2022
Basic Python Training Organized by Sri Sathya Sai Seva Organization RR District in the month of June 2022.

## Timings
1. Saturday - Evening - 6pm to 8pm
2. Sunday - Morning - 8am to 10am

# Setting up git and github, python 3.10, VS Code
1. [programming knowledge channel - How to Install Git on Windows 10 + Setting Up Git and GitHub on Windows 10](https://www.youtube.com/watch?v=bb_LoXAC-zE)
2. [How to install python 3.10 on windows 10/11](https://www.youtube.com/watch?v=AwIXfaGEN4c)
3. [How to install visual studio code on windows 10/11](https://www.youtube.com/watch?v=JPZsB_6yHVo)

## List of Topics that will be covered under this training <a name="top"></a>

1. [Let's begin the Python Show](#1)
	* [History of Python](#1.1)
	* [What is Python](#1.2)
	* [Applications of Python](#1.3)
	* [How do programming languages support problem decomposition](#1.4)
	* [What is an interpreter](#1.5)
	* [How To Get An Interpreter](#1.6)
	* [Comparison of python with other Languages](#1.7)
	* [Famous and Most used versions of python](#1.8)
	* [Why should we learn Python](#1.9)
2. About Python
	* Indentation
	* Continuation lines
	*  Command line interface coding
	* Writing python scripts in a file and running it in the command line
	interface
	* Commenting in python
	*  Debugging the code 
	*  Print function
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
	* Integers
	* Floating point
	*  Complex
	* String
	* bool
5. User Input
	* Input function
	* Command line parameters
6. Operators
	* Numeric 
	* Comparison
	*  Identity
	* Membership
	* Assignment
	*  Logical
7. Conditional statements
	* If
	* If else
	* Nested If elif else
8. Loops
	* While
	*  for
9.  Lists
	* list comprehension 
10. Tuples 
11. Dictionaries
12. File Handling
	* Read 
	*  Write
	* delete
13. Functions
14. Exception Handling
15. Modules
16. Namespace
17. Packages
18. Built in tools
19. repr()
20. difference between running the code in vs code and jupyter notebook
22. assert (basic debugging) - to set a breakpoint
23. What editors are required to use in python 

### **1. Let's begin the Python Show** <a name="1"></a>

## **History of Python** <a name="1.1"></a>

**Python** was developed by ***Guido van Rossum*** and was released first on **February 20, 1991** (31 years ago). It is one of the most widely-used and loved programming languages. It is also a **free** and **open-source language** with very simple and clean syntax.

### **What is Python?** <a name="1.2"></a>

1. **Python** is a **general-purpose high-level** programming language. Being a general-purpose language, it can be used to build almost any type of application with the right **tools** or **libraries**. 
2. Its standard library is large and comprehensive. This makes it easy for **developers** to learn python. 
3. Additionally, python supports **objects**, **modules**, **threads**, **exception-handling**, and **automatic memory management** which help in modeling real-world problems and building applications to solve these problems. 
4. Python is also used in **Machine Learning** ,  **Artificial Intelligence** , **Web Development**, **Web Scraping**, and various other domains.

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
  >Scons, Buildbot, Apache Gump, Round up, Trac.
<br />

[go to List of Topics](#top)

<br />
### How do programming languages support problem decomposition? <a name="1.4"></a>

1. **Python** supports **multiple** programming paradigms and features a fully dynamic type system and automatic memory management, similar to Perl, Tcl etc. Like other dynamic languages. Python is often used as a **scripting language**.
2. If you have to work with several C libraries, and the usual is order of C is
	> write code -> compile it -> test it -> re-write -> re-compile the code -> re-test.
	* So, The cycle is slow. You need to develop **software** more quickly. Possibly, perhaps you have written a program that could use an **extension language**, and you do not want to design a language, write and debug an interpreter for it, then tie it into your application.

3. **Python** allows you to split up your big program (program with many lines of code) into modules that can be **reused**, even into other Python programs as well. It comes with a **large collection** of standard modules that you can use as the basis of your programs, instead of writing code for each and everything from scratch.
4. There are also built-in modules that provide things like file I/O, system calls, sockets, and even interfaces to graphical user interface toolkits like Tk.

<br />

### What is an interpreter? <a name="1.5"></a>

1. An **interpreter** is a program that reads and executes code. This includes source code, pre-compiled code, and scripts. 
2. Common interpreters include Perl, Python, and Ruby interpreters, which execute Perl, Python, and Ruby code respectively. 
3. If we write a Python code in a text file with a name like hello.py. How does that code Run? There is a program installed on your computer named "python3" or "python", and its job is to look at and run your Python code. This type of program is called an "interpreter".

<br />

### How To Get An Interpreter? <a name="1.6"></a>

1. There are 2 easy ways to get the interpreter:

	  -  Open a command-line terminal. **Mac** : run the "Terminal" app in the Utilities folder. **Windows**: type "powershell" in the lower left, this opens the Windows command line terminal. In the terminal type the command "python3" ("python" on Windows, or sometimes "py"). This runs the interpreter program directly. On the Mac type ctrl-d to exit (on Windows ctrl-z).

	  - If you have **PyCharm** installed, at the lower-left of any window, click the Python Console tab. Or use the Tools > Python Console menu item to open an interpreter window within PyCharm.

2. When commands are read from a **tty**, the interpreter is said to be in **interactive** mode. In this mode it prompts for the next command with the primary prompt, usually three greater-than signs **(‘>>> ‘)**; 
3. For continuation lines it prompts with the secondary prompt, by default three dots **(‘...’)**. The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt.

4. Continuation lines are needed when entering a multi-line construct. As an example, look at this if statement:

![](https://github.com/saikrishnavadali05/python3_ebook/blob/master/Images/Screenshot%202022-01-31%20110438.jpg?raw=true)


### Comparison of python with other Languages? <a name="1.7"></a>
  
Column | Python | Java   | C++    | C 
:----- | :----: | -----: | :----: | -----:
Code Executor | Interpreter| Compiler | Compiler | Compiler
Learning and Coding Difficulty Level | Very Easy | Medium | Medium  | Easy
Number of Lines of Code (SLOC)  | Very less  | Less | Many | Extremely Many
Costs incurred to Build Applications  | Less Expensive  | Expensive | More expensive  | Most expensive
Availability of Learning and Reusable Resources  | High  | High | Less  | Less
  
<br />

[go to List of Topics](#top)

<br />
 
### Famous and Most used versions of python? <a name="1.8"></a>

They are two versions
1. Version 2
2. Version 3

* The main difference between version 2 and version 3 is **stablity of the code increases** and they are some changes in the syntax and also increase in **speed of execution of code**. So, Now version 2 has no support or resources so everyone should have latest version in their Local system.
  
 <br />

### Why should we learn Python? <a name="1.9"></a>
  
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

		**4.27 lpa ----> 9.09 lpa ----> 11.5 lpa**

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

The best and most productive field to flourish today is **web development** using python.

[go to List of Topics](#top)

<br />
