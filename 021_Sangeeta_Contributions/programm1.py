#using For loop

test_string = "Love All Serve All Help Ever Hurt Never"

# using split() 
# to extract words from string 
res = test_string.split()     
# printing result 
print ("\nThe words of string are")
for i in res:
    print(i)




#using while loop

res= test_string.split()
print(res)
i = 0
while i < len(res):
   print(res[i])     # printing result 
   i += 1
