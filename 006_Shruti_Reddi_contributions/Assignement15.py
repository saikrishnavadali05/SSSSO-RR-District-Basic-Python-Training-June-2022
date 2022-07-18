#Write a function calculate()
#  such that it can accept two variables and 
# calculate the addition, multiplication of them. 
# The result must be returned a single return call. 


    
NumList1 = [10, 20, 30]
NumList2 = [5, 2, 3]
add = []
sub = []
multi = []
div = []
mod = []
expo = []
 
for j in range(3):
    add.append( NumList1[j] + NumList2[j])
    sub.append( NumList1[j] - NumList2[j])
    multi.append( NumList1[j] * NumList2[j])
    div.append( NumList1[j] / NumList2[j])
    mod.append( NumList1[j] % NumList2[j])
    expo.append( NumList1[j] ** NumList2[j])
 
print("\nThe List Items after Addition =  ", add)
print("The List Items after Subtraction =  ", sub)
print("The List Items after Multiplication =  ", multi)
print("The List Items after Division =  ", div)
print("The List Items after Modulus =  ", mod)
print("The List Items after Exponent =  ", expo)