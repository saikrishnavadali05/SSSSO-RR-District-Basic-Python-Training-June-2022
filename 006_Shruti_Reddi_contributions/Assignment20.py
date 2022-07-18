#Write a script that accepts a comma separated list of characters 
# (and words) and prints an underscore _ separated 
# list of characters (and words) in the
#  sorted order as shown below :
input_list = ["b","c","a","d","a","e","b","f" ]
input_list.sort()
print(input_list)

str1 = ""
# traverse in the string 
for i in input_list:
    str1 =str1+i+" "
print(str1)
res=str1.replace(" ","_ ")
print(res)
#res = ', '.join(str1[i:i + 1] for i in range(0, len(str1), 1))
  
# printing result 
#print(res)
#res1=res.replace(",","_")
#print(res1)