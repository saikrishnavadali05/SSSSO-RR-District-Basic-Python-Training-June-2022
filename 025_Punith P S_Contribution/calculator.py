#from addition import add
#n= 4
#num1 = int(input("enter the 1st number"))
#num2 = int(input("enter the 2nd number"))
#num3 = int(input("enter the 3rd number"))
#num4 = int(input("enter the 4th number"))

#lst.insert(0,num1)
#lst.insert(1,num2)
#lst.insert(2,num3)
#lst.insert(3,num4)
#result = 0
#temp = 1
#for num in lst:
 
   
    #if num % 2 == 0:
        #result = num + result
    
#print("given numbers are odd numbers")
#print(result)

#for num in lst:  
    #if num % 2 == 0:
       #prev_num = num
       #mul_result = int((num * prev_num)/2)
        
        
#print(mul_result)
from addition import add
from multiply import multiplication
lst =[]

input_int_array = [int(x) for x in input("Enter the number").split()]
print(input_int_array)

for num in input_int_array:
    if num % 2 == 0:
        
       lst.append(num)

print(lst)
result = str(add(lst))
mul_even = str(multiplication(lst))

output_file = open('output.txt','w')
output_file.write(result)
output_file.write(mul_even)

output_file.close()
output_file = open('output.txt', 'r')
print(output_file.read())
output_file.close()

