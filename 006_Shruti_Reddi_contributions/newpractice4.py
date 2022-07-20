#totalMoney = 1000
#quantity = 3
#price = 450.00
#print("I have", totalMoney,"dollars so I can buy", quantity, "football for", price, "dollars.")
#statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
#print(statement1.format(quantity, totalMoney, price))

#Read line number 4 from the following file

#with open("text1.txt" , "r") as fp:
  #  lines=fp.readlines()

   # print(lines[3])

#fp.close()

#Print First 10 natural numbers using while loop

#i = 1
#while i <= 10:
  #  print(i)
   # i += 1

#Write a program to print the following number pattern using a loop.

#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5

#print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
#for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
   # for j in range(1, i + 1):
      #  print(j, end=' ')
    # empty line after each row
    #print("")

# s: store sum of all numbers
#s = 0
#n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
#for i in range(1, n + 1, 1):
    # add current number to sum variable
    #s += i
#print("\n")
#print("Sum is: ", s)

n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)
