#checking whether the givennumber is leapyear or not

from sys import argv

def leapyear(num):
    if((num%400)==0) and ((num%100)==0):
        return True
    elif((num%4)==0)and ((num%100)!=0):
        return True
    else:
        return False

Entered_year=int(argv[1])
if leapyear(Entered_year):
    print("{0} is Leap Year".format(Entered_year))
else:
     print("{0} is Not aLeap Year".format(Entered_year))
