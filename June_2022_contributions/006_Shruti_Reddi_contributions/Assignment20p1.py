input_list = ["OM","SRI","SAI","RAM" ]
input_list.sort()
print(input_list)

str1 = ""
# traverse in the string 
for i in input_list:
    str1 =str1+ i +" "
print(str1)
res=str1.replace(" ","_")
print(res)

  
