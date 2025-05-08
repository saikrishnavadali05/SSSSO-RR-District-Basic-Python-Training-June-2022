#using For loop

test_string = "Love All Serve All Help Ever Hurt Never"

# using split() 
# to extract words from string 
res = test_string.split()
print(res)     
# printing result 
print ("\nThe words of string are printed using For loop")
for i in res:
    print(i)




#using while loop

res= test_string.split()
print(res)
print ("\nThe words of string are printed using While loop")
i = 0
while i < len(res):
   print(res[i])     # printing result 
   i += 1