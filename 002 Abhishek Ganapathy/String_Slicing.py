String = input("Enter a String ")
Word = input("Enter the word which you want to find ")
Count_of_Word = String.count(Word)
print("The number of times the word", Word,"appears is",Count_of_Word)
Length_of_String = len(String)
print("The Length of the String is",Length_of_String)
Index = String.index(Word)
print("The index of the alphabet is",Index)
res = "".join([item for item in String if Word.isdigit()])
print("Digits in the string are", res)
print(String.swapcase())
Reverse_String = String[::-1]
print("The reversed String is",Reverse_String)
for i in range(0,len(String)):
    print(i,"->",String[i])
Actual_String = "AbhishekGanapathy"
Modified_String = Actual_String[:8] + "." + Actual_String[8:]
print("The modified String is",Modified_String)
for i in range(0,len(Modified_String)):
    print(i,"->",Modified_String[i])
print("Id of the String is", id(String))
print("Id of the Reverse_String is", id(Reverse_String))
print("Id of the Actual_String is", id(Actual_String))
print("Id of the Modified_String is", id(Modified_String))
print("Is the String,",String,"alpha:",String.isalpha())
print("Is the Modified_String",Modified_String, "alpha:",Modified_String.isalpha())
print("Use format method")
print(f"The String is {String}")
print("The String is {}".format(String))
String1 = Modified_String[:7]
print("The Sub string is",String1)
String2 = Modified_String[-1:-17:-1]
print("The Sub string is",String2)
String3 = Modified_String[-11:-17:-1]
print("The Sub string is",String3)

