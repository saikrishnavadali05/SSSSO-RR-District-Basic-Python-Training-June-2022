def reversing_string(s1):
   sr=" "
   for i in s1:
    sr=i+sr
   print("The string after reversing is ",sr)
s=input("Enter the string")
reversing_string(s)   
