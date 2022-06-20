Principal = int(input("Enter the Principal amount "))
Period = int(input("Enter the Period "))
Rate = int(input("Enter the Rate "))

Simple_interest = (Principal*Period*Rate)/100
print("The Simple Interest is",Simple_interest)

Compound_Interest = (Principal*(1+(Rate/100))**Period)- Principal
print("The Compound Interest is",Compound_Interest)