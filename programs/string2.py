"""
Write a program to use format method to format the following 
three variables as per the expected output

given variables

totalMoney = 1000
quantity = 5
price = 200

output

I have 1000 rupees so I can buy 5 shuttles for 200 each.

"""

#solution

totalMoney = 1000
quantity = 5
price = 200
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))