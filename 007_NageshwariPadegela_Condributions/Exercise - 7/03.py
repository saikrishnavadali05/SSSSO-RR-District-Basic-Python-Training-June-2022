# Write a script that requests the user to give an input \
# and given Kilometers convert to Miles. \
# if there are more digits after decimal round to two digits

Kilometers = float(input('Enter a number of kilometers that has to be converted to miles: '))
miles = 0.621371*Kilometers
print("%f kilometers is %.2f miles"%(Kilometers, miles))
