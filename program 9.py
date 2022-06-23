s1=input("enter first string")
s2=input("enter second string")
if (len(s1)==len(s2)):
       print("string are with same length")
       result=" "
       for i in range (len(s1)):
              result=result+(s2[i]+s1[i])
              print(result)
else:
                     print("string are with different lrngth")
