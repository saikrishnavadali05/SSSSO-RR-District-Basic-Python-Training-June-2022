Provide_String = str(input("Enter the string "))
String_Without_Commas = Provide_String.replace(',','')
print("The actual string is ",Provide_String)
Sorted_Provide_String = "_".join(sorted(String_Without_Commas))
print("The sorted string is",Sorted_Provide_String)

words = [word.lower() for word in Provide_String.split()]

print("The sorted words are:")
for word in words:
   print(word)

