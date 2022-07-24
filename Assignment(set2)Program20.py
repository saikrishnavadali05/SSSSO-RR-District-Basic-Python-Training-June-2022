#20.Write a script that accepts a comma separated list of characters (and words) and prints an underscore _ separated list of characters (and words) in the sorted order as shown below :
#Input: b,c,a,d,a,e,b,f Output: a_a_b_b_c_d_e_f. Next apply this logic to words. Input : om sri sai ram. Output : om_ram_sai_sri
#SOLUTION 1:
input_list = ["b","c","a","d","a","e","b","f" ]
input_list.sort()
print(input_list)
str1 = ""
for i in input_list:
    str1 =str1+i+" "
print(str1)
result=str1.replace(" ","_ ")
print(result)


#SOLUTION 2:
input_list = ["om","sri","sai","ram" ]
input_list.sort()
print(input_list)
str1 = ""
for i in input_list:
    str1 =str1+ i +" "
print(str1)
result=str1.replace(" ","_")
print(result)