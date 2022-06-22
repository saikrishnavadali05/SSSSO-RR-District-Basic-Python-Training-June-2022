#1.	Write a program to print each word of the line in a new line using both while and for loops.#
#Input : Love All Serve All Help Ever Hurt Never
# using print fuction first

print ("love All Serve All Help Ever Hurt Never")

#uisng Escape sequences print output
#'\n' - Newline character
#'\r' - Return character
#'\b' - Backspace character
#'\' - Backslash character
#'\”' - Double quote character
#'\’' - Single quote character
#'\t' - Tab character
#'\a' - Alarm character

#'\n' - Newline character

print ("love \n All \n Serve \n All \n Help \n Ever \n Hurt \n Never")

#'\r' - Return character
#Carriage return or \r is a very unique feature of Python.
# \r will just work as you have shifted your cursor to the beginning of the string or line.

print ("love All Serve All Help Ever Hurt Never \r 1 st of all I Love python programming lanuage \r 22 june 20222")
#output=love All Serve All Help Ever Hurt Never
 #22 june 20222 Love python programming lanuage

 #'\b' - Backspace character
 #This backspace character (\b) is used to apply a backspace in string.
 #As you can clearly see that backspace meaning of your Keyboard & Python have little bit difference.
 #When you use backspace using keyboard it erases characters & space both,
 #  while when you use backspace in python it only erases space & shift string.

print(" Hii\b")
#output = Hii

print(" Hii Raj")
#output = Hii Raj
print(" Hii\b\b\b\b Raj")
#output = Raj

print(" Hii\b Raj\bRam\b manoj\b santosh")
#output = Hi RaRa mano santosh

print(" Hii\b Raj Rammm\b kanoj\b\b\b santosh")
#output = Hi Raj Ramm ka santosh

#Using a for loop
s = input("Please enter Sentence : ")
list = s.split()
print(list)

for r in list:
    print(r, '\t')

#Output 
#1 Please enter Word: Love ALL serve All Help Ever Hurt Never
#['Love', 'ALL', 'serve', 'All', 'Help', 'Ever', 'Hurt', 'Never']
#Love
#ALL
#serve
#All
#Help
#Ever
#Hurt
#Never

#2 output =Please enter Sentence : some one help me
#['some', 'one', 'help', 'me']
#some
#one
#help
#me
#3output =Please enter Sentence : not for sale
#['not', 'for', 'sale']
#not
#for
#sale

#Using a while loop, write a Python program that displays each of the characters in “Hello” on a new line, with the letter number before each character, starting at 1. e.g.
#example
#1: H
#2: e
#3: l etc.
#This is what I have so far:
 
 #what is  enumerate function
 #The enumerate function in Python converts a data collection object into an enumerate object. 
 # Enumerate returns an object that contains a counter as a key for each value within an object,
 #  making items within the collection easier to access.

 #simple using enumerate, for example
word="Hello"
for index,letter in enumerate(word,1):
    print(index,":",letter)
#output =
#1 : H
#2 : e
#3 : l
#4 : l
#5 : o
